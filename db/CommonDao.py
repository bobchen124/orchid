#-*- encoding:UTF-8 -*-

'''
Created on 2013-1-6
@author: Bob
'''

from db.TableManager import DBTableManager

db_tm = DBTableManager()

class BaseDao():
    
    def __init__(self, collection):
        self.collection = collection;
    
    def find(self, querystr=None):
        if (None == querystr):
            return self.collection.find()
        
        return self.collection.find(querystr)
    
    def findSort(self, querystr, sorts,limit):
        return self.collection.find(querystr).sort(sorts).limit(limit)
    
    def findOne(self, querystr=None):
        if (None == querystr):
            return self.collection.find_one()
        
        return self.collection.find_one(querystr)
    
    def update(self, obj, value,flag=False):
        if flag:
            return self.collection.update(obj, value, flag)
        return self.collection.update(obj, value)
    
    def save(self, obj):
        self.collection.save(obj)
        
    def remove(self,obj):
        self.collection.remove(obj)
    
