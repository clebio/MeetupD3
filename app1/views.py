from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response
from app1.models import Member
from meetupD3 import meetup
import datetime

def home(request):
    now = datetime.datetime.now()
    html = "<html><body><h1>Meetup D3 Visualizer</h1><br /><p>The time now is %s.<p></body></html>" % now
    return HttpResponse(html)

def members(request, group_id):
    mems = meetup.getMembers(group_id)
    return render_to_response('app1/members.html', {'members': mems})
