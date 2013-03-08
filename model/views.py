#-*- encoding:UTF-8 -*-

from django.shortcuts import render_to_response
from bizs import handlers
from django.http import HttpResponse
import urllib2
from django.views.decorators.csrf import csrf_exempt
from django.utils import simplejson
from orchid import settings

#live_domain = "livelist.uubridge.net"
live_domain = settings.DOMAIN

def get_live(request,uid='1000',uname='guest'):
    #html = get_template('live.html')
    token = request.GET.get('token','token')
    token = urllib2.quote(token.encode("utf8"))
    #result_list = findLiveRoom()
    page_result = {"userid":uid,"username":uname,"token":token,"domain":live_domain}
    
    page_result['live_level1'] = handlers.findLiveRoom('ky',uid)
    page_result['live_level5'] = handlers.findLiveRoom('lx',uid)
    page_result['live_level6'] = handlers.findLiveRoom('qt',uid)
    page_result['live_level4'] = handlers.findLiveRoom('jy',uid)
    page_result['today_live'] = handlers.findTodayLive()
    #live_name = result_list[0]['courseName']
    return render_to_response('live.html',page_result)

#print handlers.findLiveRoom()

def get_token(request,uid,uname):
    html = handlers.getToken(uid, uname)
    return HttpResponse(html)

def join_liveRoom(request,uid='1000',uname=''):
    roomId = request.GET.get('roomid','roomid')
    token = request.GET.get('token','token')
    
    if uid == '1000' and token =='token':
        return render_to_response('room/login.html',{"roomid":roomId})
    
    token = urllib2.quote(token.encode("utf8"))
    
    avatar = ''
    #user_profile = usrcache.findUserById(uid)
    #if 'profile' in user_profile:
        #avatar = user_profile['profile']['avatar']
    #result_list = handlers.findLiveRoom()
    return render_to_response('live/orchid.html',{"userid":uid,"username":uname,"token":token,"roomid":roomId,'avatar':avatar})

@csrf_exempt
def love_room(request):
    uid = request.POST.get('uid','1000')
    roomid = request.POST.get('roomid','room')
    handlers.loveRoom(roomid, uid, 1)
    return HttpResponse(simplejson.dumps({'result':'ok'}), mimetype="application/json") 

def show_room(request, uid='1000', uname=''):
    token = request.GET.get('token','token')
    token = urllib2.quote(token.encode("utf8"))
    print token
    roomId = request.GET.get('roomid','')
    records = handlers.findRoomRecord(roomId)
    room = handlers.showRoom(roomId, uid,2)
    interest = handlers.findInterest(room['roomId'], room['courseClass'])
    
    return render_to_response('room/room.htm', {"room":room,"userid":uid,"token":token,"username":uname,"domain":live_domain,"records":records,"interests":interest})
