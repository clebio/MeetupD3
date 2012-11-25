import json
import urllib
import os.path
    
_apiKey = ""
_basepath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '/'
_endpoint = 'https://api.meetup.com/' 
_apiFile = _basepath + 'apiKey.txt'
with open(_apiFile) as x: _apiKey = x.read().rstrip()

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

def _get_data(target, params, format='None'):
    _params = {}
    _params['key'] = _apiKey
    _params.update(params)
    url = _endpoint + target + '?' + urllib.urlencode(_params) + "&offset=%s"    
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
            results = json.loads(s, object_hook=hooker)['results']
        except Exception:
            print("no 'results' key in response")
            results = []
        if len(results) == 0:
            break
        data.extend(results)
        offset += 1
        if format == 'json':
            data = json.dumps(data)
    return data

# Some of the API endpoints have the '2/' prefix, while other don't. Thus, different calls.
def getEventAttendees(eventId):
    return  _get_data('rsvps', {'event_id': eventId })

def getEvents(group_id):
    events =  _get_data('2/events', {'group_id': group_id, 'status': 'past', 'desc': 'true', })
    return events

def getRsvps(event_id):
    population = _get_data('2/rsvps', {'event_id': event_id })
    return [p for p in population if p['response'] == 'yes']

def getMembers(group_id):
    return _get_data('2/members', {'group_id': group_id })

def getProfiles(member_id):
#    _params['after'] = '3m'
    return _get_data('2/profiles', {'member_id': member_id })

def getGroups(group_id):
    return _get_data('2/groups', {'group_id': group_id })
    
def getGroupsByTopics(topic):
    return _get_data('2/groups', {'topic': topic })
