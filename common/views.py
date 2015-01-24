from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import RequestContext


def calendar(request):

    return render(request, "calendar/calendar.html")


def handler404(request):
    response = render_to_response('common/404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('common/500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response