'''
Created on 2013-1-9
@author: Bob
'''

from functools import wraps
import hashlib

caches_map = {}

def cacheManager(func):
    @wraps(func)
    def cacheToken(uid,username):
        map_key = uid + '-' + username
        #if map_key not in caches_map:
        caches_map[map_key] = func(uid,username)
        return caches_map[map_key]
    
    return cacheToken

@cacheManager
def getAuthToken(uid,username):
    encrypt_md = hashlib.md5()
    encrypt_md.update(uid)
    encrypt_md.update(':UUBRIDGE:')
    encrypt_md.update(username)
    return encrypt_md.hexdigest()

def authToken(uid,username,token):
    map_key = uid + '-' + username
    if map_key not in caches_map:
        return False
    token_value = caches_map[map_key]
    return True if token_value == token else False