#-*- encoding:UTF-8 -*-

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.utils import simplejson
from util.uploads import do_upload, image_cut
from util import utils
from bizs.singletons import Room, UserManager
from orchid import settings
import urllib2
from manger import bussness

live_domain = settings.DOMAIN

def open_manager(request):
    users = UserManager().getUsers()
    return render_to_response('manage/manage.html',{"domain" : live_domain,"users":users})

@csrf_exempt
def login(request):
    name = request.POST.get('name','')
    passwd = request.POST.get('pwd','')
    if ("admin_live" == name and "uubridge_live" == passwd):
        return HttpResponse(simplejson.dumps({'result':'ok'}), mimetype="application/json") 
    
    return HttpResponse(simplejson.dumps({'result':'no'}), mimetype="application/json") 

@csrf_exempt  
def upload_image(request):  
    response = HttpResponse()  
    response['Content-Type']="text/javascript"  
    ret = ""          
    temp_file = request.FILES.get("Filedata",None)          
    if temp_file:              
        name = do_upload(temp_file)
        if name != "":
            ret =  name  
        
    response.write(ret)  
    return response  

@csrf_exempt 
def save_image(request):
    name = request.POST.get('name','')
    x = request.POST.get('x','')
    y = request.POST.get('y','')
    #x2 = request.POST.get('x2','')
    #y2 = request.POST.get('y2','')
    w = request.POST.get('w','')
    h = request.POST.get('h','')
    image_cut(name,x,y,w,h)
    
    return HttpResponse(simplejson.dumps({'result':'ok'}), mimetype="application/json") 

@csrf_exempt 
def save_room(request):
    params = {}
    
    courseName = request.POST.get('courseName','')
    params['courseName'] = courseName
    openTime = request.POST.get('openTime','')
    params['openTime'] = utils.mktimes(openTime)
    #print params['openTime']
    
    courseTime = request.POST.get('time','')
    params['courseTime'] = int(courseTime)
    courseIntro = request.POST.get('courseIntro','')
    params['courseIntro'] = courseIntro
    
    cover = request.POST.get('cover','')
    params['coverPath'] = cover
    adminUser = request.POST.get('roomAdmin','')
    params['adminUser'] = adminUser
    
    courseClass = request.POST.get('courseClass','')
    params['courseClass'] = courseClass
    rommNum = request.POST.get('rommNum','')
    params['num'] = int(rommNum)
    
    roomId,createTime = utils.getRoomIdAndTime()
    params['roomId'] = roomId
    params['createTime'] = createTime
    params['status'] = 0
    params['isLive'] = 0
    params['isRecord'] = 0
    params['browse'] = 0
    
    if Room().saveRoom(params):
        return HttpResponse(simplejson.dumps({'result':True}), mimetype="application/json")
    
    return HttpResponse(simplejson.dumps({'result':False}), mimetype="application/json") 

@csrf_exempt 
def add_admin(request):
    uid = request.POST.get('uid','')
    name = request.POST.get('name','')
    
    user_admin = {"userid":uid, "username":name}
    if UserManager().saveUser(user_admin):
        return HttpResponse(simplejson.dumps({'result':True}), mimetype="application/json") 
    
    return HttpResponse(simplejson.dumps({'result':False}), mimetype="application/json") 

@csrf_exempt
def admin_course(request):
    response = HttpResponse()  
    response['Content-Type']="text/javascript"  
     
    page = request.POST.get('page','1')
    #print 'page = ' + page
    rp = request.POST.get('rp','10')
    #print 'rp = ' + rp
    sortName = request.POST.get('sortname','createTime')
    #print 'sortName = ' + sortName
    sortOrder = request.POST.get('sortorder','ASC')
    query = request.POST.get('query','')
    query = urllib2.quote(query.encode("utf8"))
    #qType = request.POST.get('qtype','')
    #print 'sortOrder = ' + sortOrder
    json_result = bussness.findRoomByPage(rp, page, sortName, sortOrder)
    #print 'json_result = ' + json_result
    response.write(json_result) 
    response.flush()
    response.close() 
    return response  

@csrf_exempt
def delRoom(request):
    roomId = request.POST.get('roomId','')
    bussness.deleteRoom(roomId)
    return HttpResponse()
