#-*- encoding:UTF-8 -*-
'''
Created on 2013-1-22
@author: Bob
'''

import uuid
import time

def getUUID():
    return str(uuid.uuid1()).replace("-","").upper()

def getCurrTime():
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

def mktimes(datastr):
    return time.mktime(time.strptime(datastr,"%Y-%m-%d %H:%M"))
    
def getRoomIdAndTime():
    roomId = str(uuid.uuid1()).replace("-","").upper()
    currTime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    return roomId, currTime

def getLocaltime(tnum):
    return time.localtime(tnum)

def getWeekday(num):
    a = u'星期天,星期一,星期二,星期三,星期四,星期五,星期六'.split(',')
    return a[num]

def getRoomtime(tnum, interval):
    ltime = getLocaltime(tnum)
    date_str = time.strftime('%Y年%m月%d日',ltime)
    #print date_str
    wd_num = time.strftime('%w', ltime)
    wd_str = getWeekday(int(wd_num))
    #print wd_str
    begin_str = time.strftime('%H:%M', ltime)
    #print begin_str
    ltime = getLocaltime(tnum+interval)
    end_str = time.strftime('%H:%M', ltime)
    #print end_str
    return date_str,wd_str,begin_str,end_str

def getRecordDesc(tk):
    now_time = time.time()
    interval = now_time - tk
    if  interval < 60:
        return str(int(interval)) + '秒前'
    elif interval >= 60 and (interval/60) < 60 :
        return str(int(interval//60)) + '分钟前'
    elif (interval/60) >= 60 and (interval/3600) <= 24:
        return str(int((interval//3600))) + '小时前'
    else:
        return time.strftime("%Y-%m-%d", getLocaltime(tk))
    
def getTodayTime():
    today = time.strftime("%Y-%m-%d",time.localtime())
    today_begin = today + " 00:00:00"
    today_end = today + " 23:59:59"
    
    beginTime = time.mktime(time.strptime(today_begin, "%Y-%m-%d %H:%M:%S"))
    endTime = time.mktime(time.strptime(today_end, "%Y-%m-%d %H:%M:%S"))
    #print today,today_begin,today_end
    #print time.mktime(time.localtime()),beginTime,endTime
    return beginTime, endTime

def getStarttime(tnum):
    ltime = getLocaltime(tnum)
    start_str = time.strftime('%H:%M', ltime)
    #print end_str
    return start_str

#print getTodayTime()
#print getStarttime(1362537000)
#print getRoomtime(1362537000.0,0)