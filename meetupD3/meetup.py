import json
import urllib
import os.path
    
_apiKey = ""
_basepath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '/'
_endpoint = 'https://api.meetup.com/' 
_apiFile = _basepath + 'apiKey.txt'
with open(_apiFile) as x: _apiKey = x.read().rstrip()
_params = {
    "key": _apiKey,
}

def _get_data(target, _params):
    url = _endpoint + target + '?' + urllib.urlencode(_params) + "&offset=%s"    
    data = []
    offset= 0
    results = {'stub': 'nil'}
    while len(results):
        response = urllib.urlopen(url%offset)
        s = unicode(response.read(), errors="ignore")
        results = json.loads(s)
        if results.has_key('results'):
            results = results['results']
        else:
            return results
        data.extend(results)
        offset += 1
        print url%offset
    return data

def getEventAttendees(eventId):
    _params['event_id'] = eventId
    people = _get_data('rsvps', _params)
    return people

def getEvents(group_id):
    _params['group_id'] = group_id
    return _get_data('2/events', _params)

def getRsvps(event_id):
    _params['event_id'] = event_id
    population = _get_data('2/rsvps', _params)
    return [p for p in population if p['response'] == 'yes']

def getMembers(group_id):
    _params['group_id'] = group_id
    people = _get_data('2/members', _params)
    return people

def getProfiles(member_id):
    _params['member_id'] = member_id
#    _params['after'] = '3m'
    return _get_data('2/profiles', _params)

def getGroups(searchTerms):
    _params['topic'] = searchTerms
    return _get_data('2/groups', _params)
    
