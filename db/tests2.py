#-*- encoding:UTF-8 -*-

'''
Created on 2013-1-29
@author: Bob
'''

import time
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

'''
openTime = time.mktime(time.strptime('2013-03-09 13:00',"%Y-%m-%d %H:%M"))
conn.orchid.course.update({"roomId":"84D07C06856411E293DDD067E5F1DAF3"},{"$set":{"openTime":openTime}})
openTime = time.mktime(time.strptime('2013-03-09 11:00',"%Y-%m-%d %H:%M"))
conn.orchid.course.update({"roomId":"BD41DB34856411E293DDD067E5F1DAF3"},{"$set":{"openTime":openTime}})
openTime = time.mktime(time.strptime('2013-03-09 12:00',"%Y-%m-%d %H:%M"))
conn.orchid.course.update({"roomId":"13BF4D16856511E293DDD067E5F1DAF3"},{"$set":{"openTime":openTime}})

openTime = time.mktime(time.strptime('2013-03-09 17:00',"%Y-%m-%d %H:%M"))
conn.orchid.course.update({"roomId":"557F88C4856511E293DDD067E5F1DAF3"},{"$set":{"openTime":openTime}})
openTime = time.mktime(time.strptime('2013-03-09 16:00',"%Y-%m-%d %H:%M"))
conn.orchid.course.update({"roomId":"0CA55628856611E293DDD067E5F1DAF3"},{"$set":{"openTime":openTime}})
openTime = time.mktime(time.strptime('2013-03-09 18:00',"%Y-%m-%d %H:%M"))
conn.orchid.course.update({"roomId":"474A7330856611E293DDD067E5F1DAF3"},{"$set":{"openTime":openTime}})

openTime = time.mktime(time.strptime('2013-03-09 10:00',"%Y-%m-%d %H:%M"))
conn.orchid.course.update({"roomId":"4295F6C4856711E293DDD067E5F1DAF3"},{"$set":{"openTime":openTime}})
openTime = time.mktime(time.strptime('2013-03-09 18:00',"%Y-%m-%d %H:%M"))
conn.orchid.course.update({"roomId":"D820FCC0856711E293DDD067E5F1DAF3"},{"$set":{"openTime":openTime}})
openTime = time.mktime(time.strptime('2013-03-09 09:00',"%Y-%m-%d %H:%M"))
conn.orchid.course.update({"roomId":"1156ADA6856711E293DDD067E5F1DAF3"},{"$set":{"openTime":openTime}})

openTime = time.mktime(time.strptime('2013-03-09 14:00',"%Y-%m-%d %H:%M"))
conn.orchid.course.update({"roomId":"2ACE8AFA856811E293DDD067E5F1DAF3"},{"$set":{"openTime":openTime}})
openTime = time.mktime(time.strptime('2013-03-09 14:00',"%Y-%m-%d %H:%M"))
conn.orchid.course.update({"roomId":"7579B62C856511E293DDD067E5F1DAF3"},{"$set":{"openTime":openTime}})
openTime = time.mktime(time.strptime('2013-03-09 15:00',"%Y-%m-%d %H:%M"))
conn.orchid.course.update({"roomId":"BED2DC22856511E293DDD067E5F1DAF3"},{"$set":{"openTime":openTime}})

openTime = time.mktime(time.strptime('2013-03-09 20:00',"%Y-%m-%d %H:%M"))
conn.orchid.course.update({"roomId":"133E3E4A859911E293DDD067E5F1DAF3"},{"$set":{"openTime":openTime}})
'''

openTime = time.mktime(time.strptime('2013-03-07 14:00',"%Y-%m-%d %H:%M"))
conn.orchid.course.update({"roomId":"754FD4EC84AC11E293DDD067E5F1DAF3"},{"$set":{"openTime":openTime}})
