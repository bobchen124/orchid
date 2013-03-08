'''
Created on 2013-1-6
@author: Bob
'''

#-*- encoding:UTF-8 -*-

from db.settings import mongodb_conn,DATABASES

db_name = DATABASES['DBNAME'];

class DBTableManager():
    
    def __init__(self):
        self.db = mongodb_conn[db_name];
    
    '''
    get course collection
    '''
    def getCourseTable(self):
        return self.db[DATABASES['COURSE']]
    
    '''
    get managers collection
    '''
    def getManagerTable(self):
        return self.db[DATABASES['MANAGER']]
    
    '''
    get record collection
    '''
    def getRecordCollection(self):
        return self.db[DATABASES['RECORD']]

