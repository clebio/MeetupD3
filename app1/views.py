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
            return HttpResponseRedirect('topics/'+ escape(form.cleaned_data['topicList']) )
    else:
        form = TopicsForm()
    return render(request, 'app1/home.html', {'form': form, 'title': 'Search for groups' })

def genericView(request, target, member_id):
    pros = meetup.get_data(target, member_id)
    return render(request, 'app1/' + target + '.html', {target: pros, })

def d3View(request, t, i):
    return render(request, 'app1/d3.html', {'target': t, 'item': i})

def serveJson(request, target, item_id):
    pros = meetup.get_data(target, item_id, format='json')
    return HttpResponse(pros, content_type="application/json");

