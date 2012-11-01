from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response
from app1.models import Member
from meetupD3 import meetup
import datetime

def home(request):
    now = datetime.datetime.now()
    html = "<p>The time now is %s.<p>" % now
    return render_to_response('base.html', {'title': 'Homepage', 'content': html})

def profiles(request, member_id):
    pros = meetup.getProfiles(member_id)
    return render_to_response('app1/profiles.html', {'profiles': pros, 'title': 'Meetup Profiles for ' + member_id})

def members(request, group_id):
    mems = meetup.getMembers(group_id)
    return render_to_response('app1/members.html', {'members': mems, 'title': 'Meetup Members'})

def events(request, group_id):
    eve = meetup.getEvents(group_id)
    return render_to_response('app1/events.html', {'events': eve, 'title': 'Meetup Events for group ' + group_id})

def rsvps(request, event_id):
    rsvps = meetup.getRsvps(event_id)
    return render_to_response('app1/rsvps.html', {'rsvps': rsvps, 'title': 'RSVPs for event ' + event_id})

