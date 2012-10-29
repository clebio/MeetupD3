from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from app1.models import Member

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'meetupD3.views.home', name='home'),
    url(r'^members/$', ListView.as_view(
        model=Member,
    )),

    url(r'^admin/', include(admin.site.urls)),
)
