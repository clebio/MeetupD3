from django.conf.urls import patterns, include, url
from django.http import HttpResponse

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
		# TODO: repace all these views with a general one taking first word as argument (see 'views.py')
    url(r'^(\w+)/(\d+|\w+)/$', 'app1.views.genericView'),
    url(r'^d3/$', 'app1.views.d3'),
    url(r'^dummy/$', 'app1.views.dummy', ),
    url(r'^$', 'app1.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
