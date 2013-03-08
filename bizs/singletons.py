'''
Created on 2013-1-18
@author: Bob
'''
#-*- encoding:UTF-8 -*-

import urllib2
import json
from functools import wraps
from db.CommonDao import BaseDao, db_tm
import time

USER_NAME_PATH = "http://192.168.80.24:8082/UserService/getbaseprofile?username="
USER_ID_PATH = "http://192.168.10.218:9090/UserService/getuserinfo?userid="

def findUserprofileByName(uname):
    user_req = urllib2.Request(USER_NAME_PATH + uname)
    user_resp = urllib2.urlopen(user_req)
    user_result = user_resp.read()
    return json.loads(user_result)

def findUserinfo(uid):
    user_req = urllib2.Request(USER_ID_PATH + uid)
    user_resp = urllib2.urlopen(user_req)
    user_result = user_resp.read()
    return json.loads(user_result)

def singleton(cls):
    @wraps(cls)
    def clswarp(*args, **kwargs):
        o_cls = getattr(cls, "__instance__", None)
        if not o_cls:
            o_cls = cls(*args, **kwargs)
            cls.__instance__ = o_cls
        return o_cls
    
    return clswarp

@singleton     
class User(object):
    
    profile_map = {}
    
    def __init__(self):
        pass
        
    def findProfileById(self, uid):
        if uid not in User.profile_map:
            User.profile_map[uid] = findUserinfo(uid)['profile']
        return User.profile_map[uid]
    
@singleton     
class UserManager(object):
    
    def __init__(self): 
        self.dao = BaseDao(db_tm.getManagerTable())
    
    def saveUser(self,user_obj): 
        try:
            self.dao.save(user_obj)
            return True
        except:
            return False 
         
    def getUsers(self):
        return  self.dao.find()
        
@singleton        
class Room(object):
    #room_map = {}
    def __init__(self):
        self.dao = BaseDao(db_tm.getCourseTable())
        
    def findOne(self,roomid):
        #if roomid not in Room.room_map:
            #Room.room_map[roomid] = self.dao.findOne({'roomId' : roomid})
        return self.dao.findOne({'roomId' : roomid})
        
    def updateLove(self, update_obj, update_val):
        self.dao.update(update_obj, update_val)
        
    def updateViews(self,roomid):
        update_obj = {"roomId":roomid}
        update_val = {"$inc": {"browse":1}}
        self.dao.update(update_obj, update_val)
        
    def findInterestRoom(self,roomId,roomClass):
        query_dirc = {"courseClass":roomClass,"roomId":{"$ne":roomId},"status":{"$ne":2}}
        return self.dao.find(query_dirc).sort("browse",-1).limit(4)
        #return self.dao.findSort(query_dirc, {'browse':-1}, 4)
    
    def saveRoom(self,dict_obj):
        try:
            self.dao.save(dict_obj)
            return True
        except:
            return False
    
    def findRoomPaging(self,limits,skips,sortName,sortOrder,query=None,qType=None):
        result = self.dao.find().skip(skips).limit(limits).sort(sortName,sortOrder)
        return result
    
    def delete(self,roomId):
        self.dao.remove({"roomId":roomId})
        
    def findToadyLive(self,startTime,endTime):
        query_dirc = {"openTime":{"$gte":startTime,"$lte":endTime}}
        return self.dao.find(query_dirc).sort('openTime',1)
    
class RecordHandler(object):
    
    def __init__(self):
        self.dao = BaseDao(db_tm.getRecordCollection())
    
    def addRecord(self,params):
        self.dao.save(params)
    
    def findRecord(self,roomid):
        return self.dao.findOne({'roomId' : roomid})
    
    def updateRecord(self, rid, uid, rtype):
        if uid == '1000' or uid == '':
            return
        
        tk = time.time()
        u_obj = {"roomId":rid}
        u_val = None
        if (rtype == 1):
            u_val = {"$inc":{"parts":1},"$push":{"logs":{"userid":uid,"time":tk,"desc":"1"}}} #1-love
        else:
            u_val = {"$inc":{"parts":1},"$push":{"logs":{"userid":uid,"time":tk,"desc":"2"}}} #2-brwose
        
        self.dao.update(u_obj, u_val, True)
