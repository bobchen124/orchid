'''
Created on 2013-1-28

@author: Administrator
'''

import time
import urllib2

print time.ctime(),time.time()
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(1362537000.0))
print time.strptime("2013-01-23 19:20","%Y-%m-%d %H:%M")
print time.mktime(time.strptime("2013-01-23 19:20","%Y-%m-%d %H:%M"))
print time.localtime(time.mktime(time.strptime("2013-01-23 19:20","%Y-%m-%d %H:%M")))
print time.strftime('%A',time.localtime(time.time()))

print str(int(time.time() // 3600)) + "aa"
#getRoomtime(1359444420, 60*60)

print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(1362484800.0))


t = time.mktime(time.strptime('2013-02-25 14:00',"%Y-%m-%d %H:%M"))
t = t + 3600 * 24
print time.strftime('%Y-%m-%d %H:%M',time.localtime(1362486600.0))

print time.strftime("%Y-%m-%d",time.localtime())

token = 'PLhWLe93alQcCT3vq+Sjpg=='
print urllib2.quote(token.encode("utf8"))