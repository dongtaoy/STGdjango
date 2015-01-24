__author__ = 'zhangjingyuan'

from django.conf.urls import patterns, url
from django.views.generic import ListView
from django.contrib.auth.decorators import permission_required, login_required
from system.models import Icon
from system.icon.views import IconUpdateView, IconCreateView, IconDeleteView

urlpatterns = patterns(
    '',
    url(r'^$', login_required(ListView.as_view(
        model=Icon,
        context_object_name='icons',
        template_name='system/icon/icon.list.html'
    )), name='icon.list'),

    url(r'^add/$', permission_required('system.add_icon')(IconCreateView.as_view()), name='icon.add'),

    url(r'^mod/(?P<icon>\d+)/$', permission_required('system.change_icon')(IconUpdateView.as_view()), name='icon.mod'),

    url(r'^del/(?P<icon>\d+)/$', permission_required('system.delete_icon')(IconDeleteView.as_view()), name='icon.delete'),






)