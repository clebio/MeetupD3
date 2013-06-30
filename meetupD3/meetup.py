import json
import urllib
import os.path
    
_apiKey = ""
_basepath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '/'
_endpoint = 'https://api.meetup.com/' 
_apiFile = _basepath + 'apiKey.txt'
with open(_apiFile) as x: _apiKey = x.read().rstrip()

targets = {
		'attendees': { 'target': 'rsvps', 'arg': 'event_id' },
		'events': { 'target': '2/events', 'arg': 'group_id', 'status': 'past', 'desc': 'true', 'value': 'yes_rsvp_count'},
		'rsvps': {'target': '2/rsvps', 'arg': 'event_id', 'value': 'mtime' },
		'members': {'target': '2/members', 'arg': 'group_id', 'value': 'joined'},
		'profiles': {'target': '2/profiles', 'arg': 'member_id', 'value': 'visited', },
		'groups': {'target': '2/groups', 'arg': 'group_id', 'value': 'members'},
		'topics': {'target': '2/groups', 'arg': 'topic', 'value': 'members' }
	}

destinations = {
		'attendees': {},
		'events': { 'd3_name': 'name', 'd3_value': 'yes_rsvp_count', 'd3_url': 'event_url'},
		'rsvps': {'d3_name': 'member name', 'd3_value': 'created' },
		'members': {'target': '2/members', 'arg': 'group_id', 'value': 'joined'},
		'profiles': {'d3_name': 'group name', 'd3_value': 'created' },
		'groups': {'target': '2/groups', 'arg': 'group_id', 'value': 'members'},
		'topics': {'target': '2/groups', 'arg': 'topic', 'value': 'members' }
	}


def get_value_key(dest):
    return targets[dest]['value']

def get_data(dest, arg_id, format='none'):
    _params = {}
    _params['key'] = _apiKey
    _params[targets[dest]['arg']] = arg_id
    url = _endpoint + targets[dest]['target'] + '?' + urllib.urlencode(_params) + "&offset=%s"    
    data = []
    offset= 0
    while True:
        print url%offset
        response = urllib.urlopen(url%offset)
        s = unicode(response.read(), errors="ignore")
        try:
            results = json.loads(s)['results']
        except Exception:
            print("no 'results' key in response")
            results = []
        if len(results) == 0:
            break
        if format == 'json':
            results = mediate_meetup(results, dest)
            data = json.dumps({ 'results': results })
        else:
            data.extend(results)
        offset += 1
    return data
    
def mediate_meetup(obj, destined):
    dest = destinations[destined]
    for d in dest:
        for o in obj:
            d3_item = o
            for t in dest[d].split():
                d3_item = d3_item[t]
            o[d] = d3_item
    return obj
