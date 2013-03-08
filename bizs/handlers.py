#-*- encoding:UTF-8 -*-
'''
Created on 2013-1-7
@author: Bob
'''

from db.CommonDao import BaseDao, db_tm
from bizs.caches import getAuthToken
from functools import wraps
from util import utils
from bizs.singletons import User, Room, RecordHandler
import time

def getprofile(uid):
    return User().findProfileById(uid)

def profileHandler(func):
    @wraps(func)
    def userProfile(value,uid):
        live_profile = []
        result = func(value,uid)
        
        for item in result:
            uname = item['adminUser']
            usr_profile = getprofile(uname)
            
            item['profile'] = {}
            item['profile']['avatar'] = usr_profile['avatar']
            item['profile']['nick'] = usr_profile['name']
            
            if 'reserve' in item:
                item['lovenum'] = len(item['reserve'])
                if uid in item['reserve']:
                    item['islove'] = True
            else: 
                item['lovenum'] = 0
                
            live_profile.append(item)
        return live_profile
    return userProfile

@profileHandler
def findLiveRoom(type_live,uid):
    result = BaseDao(db_tm.getCourseTable()).find({"status":{'$ne':2},"courseClass":type_live})
    return result

def joinLiveRoom():
    pass

def getToken(uid, username):
    return getAuthToken(uid, username)

def recordwrap(func):
    def addRecord(rid, uid, rtype):
        try:
            RecordHandler().updateRecord(rid, uid, rtype)
        except:
            print 'except recordwrap'
        
        return func(rid, uid, rtype)
    return addRecord

@recordwrap
def loveRoom(rid, uid,rtype=1):
    if (rid == '1000'):
        return
    update_obj = {"roomId":rid}
    update_val = {'$push':{"reserve":uid}}
    BaseDao(db_tm.getCourseTable()).update(update_obj, update_val)

def profileHandler2(func):
    @wraps(func)
    def userProfile(roomid,uid,rtype=2):
        result = func(roomid,uid,rtype)
        
        uname = result['adminUser']
        usr_profile = getprofile(uname)
            
        result['profile'] = {}
        result['profile']['avatar'] = usr_profile['avatar']
        result['profile']['nick'] = usr_profile['name']
            
        if 'reserve' in result:
            result['lovenum'] = len(result['reserve'])
            print result['reserve']
            if uid in result['reserve']:
                    result['islove'] = True
        else: 
            result['lovenum'] = 0
                
        return result
    return userProfile

@recordwrap
@profileHandler2
def showRoom(roomid,uid,rtype=2):
    room = Room().findOne(roomid)
    Room().updateViews(roomid)
    date_str,wd_str,begin_str,end_str = utils.getRoomtime(room['openTime'], room['courseTime'] * 60)
    room['date'] = date_str
    room['wd'] = wd_str
    room['btime'] = begin_str
    room['etime'] = end_str
    if 'browse' in room:
        room['browse'] = room['browse'] + 1
    else:
        room['browse'] = 1
    
    room['roomtip'] = '即将直播'
    nowtime = time.time()
    if nowtime > room['openTime'] and nowtime <= room['openTime'] + room['courseTime'] * 60:
        room['roomtip'] = '正在直播'
    elif nowtime > room['openTime'] + room['courseTime'] * 60:
        room['roomtip'] = '已经结束'
        
    return room

def roomRecord(func):
    limit = 6
    @wraps(func)
    def recordWrap(rid):
        result = func(rid)
        if result == None:
            pass
        else:
            logs = result['logs']
            for item in logs:
                usr_profile = getprofile(item['userid'])
                item['avatar'] = usr_profile['avatar']
                item['nick'] = usr_profile['name']
                
                desc = item['desc']
                item['desc'] = '报名参加' if desc == '1' else '查看课程'
                
                tk = item['time']
                item['time'] = utils.getRecordDesc(tk)
            
            result['logs'] = reversed(logs[-limit:-1]) if len(logs) > limit else reversed(logs)
        return result
    return recordWrap

@roomRecord
def findRoomRecord(rid):
    return RecordHandler().findRecord(rid)

def findInterest(roomId,roomClass):
    return Room().findInterestRoom(roomId, roomClass)

def timeHandler(func):
    @wraps(func)
    def timeProfile():
        live_today = []
        result = func()
        for item in result:
            start_str= utils.getStarttime(item['openTime'])
            item['time'] = start_str   
            live_today.append(item)
            
        return live_today
    return timeProfile 

@timeHandler
def findTodayLive():
    startTime,endTime = utils.getTodayTime()
    print startTime,endTime
    todayLives = Room().findToadyLive(startTime, endTime)
    return todayLives
