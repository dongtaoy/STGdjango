__author__ = 'zhangjingyuan'

from django.conf.urls import patterns, url
from django.views.generic import ListView
from django.contrib.auth.decorators import permission_required, login_required
from system.models import Glyphicon
from system.glyphicon.views import GlyphiconUpdateView, GlyphiconCreateView, GlyphiconDeleteView

urlpatterns = patterns(
    '',
    url(r'^$', login_required(ListView.as_view(
        model=Glyphicon,
        context_object_name='glyphicons',
        template_name='system/glyphicon/glyphicon.list.html'
    )), name='glyphicon.list'),

    url(r'^add/$', permission_required('system.add_glyphicon')(GlyphiconCreateView.as_view()), name='glyphicon.add'),

    url(r'^mod/(?P<glyphicon>\d+)/$', permission_required('system.change_glyphicon')(GlyphiconUpdateView.as_view()), name='glyphicon.mod'),

    url(r'^del/(?P<glyphicon>\d+)/$', permission_required('system.delete_glyphicon')(GlyphiconDeleteView.as_view()), name='glyphicon.delete'),






)