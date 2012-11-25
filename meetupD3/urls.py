from django.conf.urls import patterns, include, url
from django.http import HttpResponse

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^profiles/(\d+)/$', 'app1.views.profiles'),
    url(r'^groups/(.+)/$', 'app1.views.groups'),
    url(r'^events/(\d+)/$', 'app1.views.events'),
    url(r'^rsvps/(.+)/$', 'app1.views.rsvps'),
    url(r'^topics/(.+)/$', 'app1.views.topics'),
    url(r'^members/(\d+)/$', 'app1.views.members'),
    url(r'^d3/$', 'app1.views.d3'),
    url(r'^dummy/$', 'app1.views.dummy', ),
    url(r'^$', 'app1.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
