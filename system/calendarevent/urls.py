__author__ = 'dongtaoy'
from django.conf.urls import patterns, url
from django.contrib.auth.decorators import permission_required, login_required
from system.calendarevent.views import CalendarEventCreateView, CalendarEventUpdateView, CalendarEventDeleteView

urlpatterns = patterns(
    '',
    url(r'^list/', 'system.calendarevent.views.feed_events', name="calendarevent.feed"),

    url(r'^add/$', permission_required('system.add_calendarevent')(CalendarEventCreateView.as_view()), name='calendarevent.add'),

    url(r'^mod/(?P<calendarevent>\d+)/$',
        permission_required('system.change_calendarevent')(CalendarEventUpdateView.as_view()), name='calendarevent.mode'),

    url(r'^del/(?P<calendarevent>\d+)/$',
        permission_required('system.delete_calendarevent')(CalendarEventDeleteView.as_view()), name='calendarevent.delete'),
)