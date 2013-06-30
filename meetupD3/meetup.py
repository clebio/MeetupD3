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
		'profiles': {'target': '2/profiles', 'arg': 'member_id', 'value': 'visited', 'name': 'group.name' },
		'groups': {'target': '2/groups', 'arg': 'group_id', 'value': 'members'},
		'topics': {'target': '2/groups', 'arg': 'topic', 'value': 'members' }
	}

def _decode_list(data):
    rv = []
    for item in data:
        if isinstance(item, unicode):
            item = item.encode('utf-8')
        elif isinstance(item, list):
            item = _decode_list(item)
        elif isinstance(item, dict):
            item = _decode_dict(item)
        rv.append(item)
    return rv

def _decode_dict(data):
    rv = {}
    for key, value in data.iteritems():
        if isinstance(key, unicode):
            key = key.encode('utf-8')
        if isinstance(value, unicode):
            value = value.encode('utf-8')
        elif isinstance(value, list):
            value = _decode_list(value)
        elif isinstance(value, dict):
            value = _decode_dict(value)
        rv[key] = value
    return rv

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
            hooker = (lambda dict: dict)
            if format == 'json':
                hooker = _decode_dict
            results = json.loads(s)['results'] # , object_hook=hooker
        except Exception:
            print("no 'results' key in response")
            results = []
        if len(results) == 0:
            break
        if format == 'json':
            data = json.dumps({ 'results': results })
        else:
            data.extend(results)
        offset += 1
    return data
    
