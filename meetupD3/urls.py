from django.conf.urls import patterns, include, url
from django.http import HttpResponse

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^profiles/(\d+)/$', 'app1.views.profiles'),
    url(r'^members/(\d+)/$', 'app1.views.members'),
    url(r'^$', 'app1.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
