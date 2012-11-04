from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse
from app1.models import Member
from meetupD3 import meetup
from django import forms
from django.utils.html import escape

def home(request):
    class TopicsForm(forms.Form):
        topicList = forms.CharField(label='topic(s)')
    
    if request.method == 'POST':
        form = TopicsForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('groups/'+ escape(form.cleaned_data['topicList']) )
    else:
        form = TopicsForm()
    return render(request, 'app1/home.html', {'form': form, 'title': 'Search for groups' })

def profiles(request, member_id):
    pros = meetup.getProfiles(member_id)
    return render_to_response('app1/profiles.html', {'profiles': pros, })

def members(request, group_id):
    mems = meetup.getMembers(group_id)
    return render_to_response('app1/members.html', {'members': mems, 'title': 'Meetup Members'})

def events(request, group_id):
    eve = meetup.getEvents(group_id)
    return render_to_response('app1/events.html', {'events': eve, 'title': 'Meetup Events for group ' + group_id})

def rsvps(request, event_id):
    rsvps = meetup.getRsvps(event_id)
    return render_to_response('app1/rsvps.html', {'rsvps': rsvps, 'title': 'RSVPs for event ' + event_id})

def groups(request, search_terms):
    groups = meetup.getGroups(search_terms)
    return render_to_response('app1/groups.html', {'groups': groups, 'title': 'Groups related to the term ' + search_terms}) 
