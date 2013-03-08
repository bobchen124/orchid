#-*- encoding:UTF-8 -*-

'''
Created on 2013-2-19
@author: Bob
'''

import json
from bizs.singletons import Room

class Course():
    def __init__(self,roomId,courseName):
        self.roomId = roomId
        self.courseName = courseName
        
def findRoomByPage(rp,page,sortName,sortOrder,query=None,qType=None):
    limits = int(rp)
    skips = (int(page) - 1) * limits
    orders = -1
    if 'ASC' == sortOrder:
        orders = 1
    
    result = Room().findRoomPaging(limits, skips, sortName, orders, query, qType)
    total = result.count()
    print "total = " , total
    list_room = []
    for room in result:
        if 'roomId' not in room:
            continue
    
        course = {"roomId":room['roomId'],"courseName":room['courseName']}
        course['openTime'] = room['openTime']
        #course['courseTime'] = room['courseTime']
        s = room['status']
        
        if 0 == s:
            course['status'] = '未开始'
        elif 1 == s:
            course['status'] = '正在进行'
        elif 2 == s:
            course['status'] = '已关闭'
        else:
            course['status'] = '未开始'
            
        list_room.append(course)
    
    #print json.dumps(list_room)
    json_result = "{\"page\":" + page + ",\"total\":" + str(total) + ",\"rows\":" + json.dumps(list_room)  + "}";
    return json_result

#print findRoomByPage('10','1','op','ASC')

def deleteRoom(roomId):
    try:
        Room().delete(roomId)
    except:
        pass