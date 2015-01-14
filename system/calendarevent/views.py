__author__ = 'dongtaoy'
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from system.forms import CalendarEventForm
from system.models import CalendarEvent
from django.http import HttpResponse
from fullcalendar.util import events_to_json

class CalendarEventCreateView(SuccessMessageMixin, CreateView):
    form_class = CalendarEventForm
    template_name = 'system/calendarevent/calendarevent.edit.html'
    success_url = '/calendar/'
    success_message = '%(title)s Calendar Event created'


class CalendarEventUpdateView(SuccessMessageMixin, UpdateView):
    form_class = CalendarEventForm
    template_name = 'system/calendarevent/calendarevent.edit.html'
    success_url = '/calendar/'
    context_object_name = 'spec_calendarevent'
    pk_url_kwarg = 'calendarevent'
    model = CalendarEvent
    success_message = '%(title)s Calendar Event created'



class CalendarEventDeleteView(DeleteView):
    model = CalendarEvent
    template_name = 'common/delete.confirmation.html'
    success_url = '/calendar/'
    pk_url_kwarg = 'calendarevent'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Calendar Event deleted')
        return super(CalendarEventDeleteView, self).delete(self.request, *args, **kwargs)


def feed_events(request):
    print request
    events = CalendarEvent.objects.all()
    return HttpResponse(events_to_json(events), content_type='application/json')