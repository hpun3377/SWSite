from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.template import loader
from django.shortcuts import render_to_response
import datetime

# Create your views here.
def home(request):
    return render_to_response('index.html')

def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

# 예쁜 에러 페이지
# def hours_ahead(request, offset):
#     try:
#         offset = int(offset)
#     except ValueError:
#         raise Http404()
#     dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
#     assert False
#     html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
#     return HttpResponse(html)