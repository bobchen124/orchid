from django.conf.urls import patterns, include
#from model.views import get_live,get_token,join_liveRoom,love_room, show_room
#from model import part

#from django.conf import settings

#from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('model.views',
    # Examples:
    # url(r'^$', 'orchid.views.home', name='home'),
    # url(r'^orchid/', include('orchid.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^live/$', 'get_live'),
    (r'^live/(?P<uid>\d+)/(?P<uname>.+)/$', 'get_live'),
    (r'^getToken/(\d+)/(.+)/$', 'get_token'),
    (r'^joinlive/(\d+)/(.+)/$', 'join_liveRoom'),
    (r'^live/love/$', 'love_room'),
    (r'^room/(\d+)/(.+)/$', 'show_room'),
    (r'^manage/', include('manger.urls')),
    #(r'^manage/$', open_manager),
    #(r'^manage/login/$', login),
)

urlpatterns += patterns('model.part',
    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^part/$', 'view_part'),
    (r'^part/(\d+)/(.+)/$', 'view_part'),
    #(r'^manage/$', open_manager),
    #(r'^manage/login/$', login),
)

#urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)