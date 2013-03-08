#-*- encoding:UTF-8 -*-

'''
Created on 2013-1-29
@author: Bob
'''

import time
import json
from pymongo import Connection

hosts = '192.168.80.21'
ports = 27017
conn = Connection(host=hosts, port=ports)
#conn.orchid.course.update({"roomId":"0CB31EC06A8B11E296D34437E6561D23"},{"$set":{"courseName":"上海交通大学新闻学考研复试直播间"}})
#conn.orchid.course.update({"roomId":"932782406A8911E2BC844437E6561D23"},{"$set":{"courseName":"华东政法学院金融法律考研复试直播间"}})
#conn.orchid.course.update({"roomId":"A163F5916A8A11E2815F4437E6561D23"},{"$set":{"courseName":"上海交通大学食品科学与工程专业考研复试直播间"}})
#conn.orchid.course.update({"roomId":"D536730F6A8B11E2800D4437E6561D23"},{"$set":{"courseName":"西安交通大学金融学专业硕士考研复试直播间 "}})
#conn.orchid.course.update({"roomId":"F633538A6F6811E293DDD067E5F1DAF3"},{"$set":{"coverPath":"wotaihua.jpg"}})

#conn.orchid.course.remove({"roomId":"0CD70758809E11E293DDD067E5F1DAF3"})
#conn.orchid.course.remove({"roomId":"A37529A67B2611E293DDD067E5F1DAF3"})
#conn.orchid.course.remove({"roomId":"D536730F6A8B11E2800D4437E6561D23"})
#conn.orchid.course.remove({"roomId":"0CB31EC06A8B11E296D34437E6561D23"})

#conn.orchid.course.remove({"roomId":"005938FC821011E293DDD067E5F1DAF3"})
#conn.orchid.course.remove({"roomId":"471CEE94821211E293DDD067E5F1DAF3"})

#time.mktime(time.strptime(datastr,"%Y-%m-%d %H:%M"))
#openTime = time.mktime(time.strptime('2013-02-27 04:00',"%Y-%m-%d %H:%M"))
#ltime = time.localtime(openTime)
#print time.strftime('%H:%M', ltime)

openTime = time.mktime(time.strptime('2013-03-10 14:00',"%Y-%m-%d %H:%M"))
conn.orchid.course.update({"roomId":"2ACE8AFA856811E293DDD067E5F1DAF3"},{"$set":{"openTime":openTime}})

'''
today = time.strftime("%Y-%m-%d")
today_begin = today + " 00:00:00"
today_end = today + " 23:59:59"

beginTime = time.mktime(time.strptime(today_begin, "%Y-%m-%d %H:%M:%S"))
endTime = time.mktime(time.strptime(today_end, "%Y-%m-%d %H:%M:%S"))
endTime = endTime + 14 * 60 * 60
print beginTime,endTime

query_dirc = {"openTime":{"$gte":beginTime,"$lte":endTime}}
result = conn.orchid.course.find(query_dirc).sort('openTime',1)
print result.count()
for item in result:
    print item['roomId']
'''