# Create your views here.
from django.http import HttpResponse
import datetime

def home(request):
    now = datetime.datetime.now()
    html = "<html><body><h1>Meetup D3 Visualizer</h1><br /><p>The time now is %s.<p></body></html>" % now
    return HttpResponse(html)
