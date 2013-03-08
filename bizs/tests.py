"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

import datetime
from bizs import handlers
from time import time 
import json

t1 = datetime.datetime.now()
list_r = handlers.findLiveRoom("jy",10423)
for item in list_r:
    print item
list_r = handlers.findLiveRoom("ky",10423)
for item in list_r:
    print item
list_r = handlers.findLiveRoom("lx",10423)
for item in list_r:
    print item['adminUser']['avatar']
list_r = handlers.findLiveRoom("qt",10423)
for item in list_r:
    print item
t2 = datetime.datetime.now()
print (t2-t1).microseconds/1000

t = time()
page_result = {}    

page_result['live_level1'] = handlers.findLiveRoom('ky',10423)
page_result['live_level5'] = handlers.findLiveRoom('lx',10423)
page_result['live_level6'] = handlers.findLiveRoom('qt',10423)
page_result['live_level4'] = handlers.findLiveRoom('jy',10423)

print time() - t

s = "{\'roomAdmin\' : 11}"
print type(s)
print json.loads(s)
#handlers.loveLive('7F57AAB0A5FF4D298018804BEE7DBC79', '10425')

#tk = time.time()
#u_obj = {"roomId":'9906D7B0669C11E2BE504437E6561D23'}
#u_val = {"$inc":{"parts":1},"$push":{"logs":{"userid":'10421',"time":tk,"desc":"1"}}}
#BaseDao(db_tm.getRecordCollection()).update(u_obj, u_val, True)

#BaseDao(db_tm.getRecordCollection()).find({'roomId' : '9906D7B0669C11E2BE504437E6561D23'}).sort({"time":-1})