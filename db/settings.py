'''
    MongoDB config
'''

from pymongo import Connection

#hosts = '192.168.80.21'
DATABASES = {
    'HOST': '192.168.10.218',                     
    'PORT': 27017,
    'DBNAME': 'orchid',
    'COURSE': 'course', 
    'MANAGER': 'managers',
    'RECORD': 'record',  
    'USER': '', 
    'PASSWORD': '',       
}

#print DATABASES['HOST'], DATABASES['PORT']
mongodb_conn = Connection(host=DATABASES['HOST'],port=DATABASES['PORT'])
