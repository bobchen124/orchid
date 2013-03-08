from django.conf.urls import patterns
from manger import views

#from django.conf import settings

#from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'orchid.views.home', name='home'),
    # url(r'^orchid/', include('orchid.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^live/$', views.open_manager),
    (r'^login/$', views.login),
    (r'^upload/image/$', views.upload_image),
    (r'^upload/imagecut/$', views.save_image),
    (r'^create/room/$', views.save_room),
    (r'^add/user/$', views.add_admin),
    (r'^room/query/$', views.admin_course),
    (r'^room/delete/$', views.delRoom),
)

#urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)