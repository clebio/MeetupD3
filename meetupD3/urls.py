from django.conf.urls import patterns, include, url
from django.http import HttpResponse

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^(\w+)/(\d+|\w+)/$', 'app1.views.genericView'),
    url(r'^d3/(\w+)/(\d+|\w+)/$', 'app1.views.d3View'),
    url(r'^(\w+)/(\d+|\w+).json$', 'app1.views.serveJson'),
    url(r'^$', 'app1.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
