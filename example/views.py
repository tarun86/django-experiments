from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def hours_ahead(request, offset):
    offset = int(offset)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    #assert False
    return HttpResponse(html)
    
def hours_behind(request, offset):
    offset = int(offset)
    dt = datetime.datetime.now() - datetime.timedelta(hours=offset)
    html = "<h1>In %s hour(s) in the past, the time would be %s </h1>" % (offset, dt)
    return HttpResponse(html)

def hours_offset(request, minus_or_plus, offset):
    dt = datetime.datetime.now() - datetime.timedelta(hours=offset)            
    html = "<h1>In %s hour(s) in the past, the time would be %s </h1>" % (offset, dt)
    return HttpResponse(html)
