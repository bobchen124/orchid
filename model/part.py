'''
Created on 2013-3-7
@author: bob
'''

import urllib2
from django.shortcuts import render_to_response
from orchid import settings

live_domain = settings.DOMAIN

def view_part(request,uid='1000',uname=''):
    token = request.GET.get('token','token')
    token = urllib2.quote(token.encode("utf8"))
    return render_to_response('unversity/fspart.html',{"userid":uid,"username":uname,"token":token,"domain":live_domain})