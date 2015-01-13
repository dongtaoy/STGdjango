from django.conf.urls import patterns, url, include
from django.views.generic import ListView, TemplateView
from django.contrib.auth.decorators import permission_required, login_required
from client.coe.views import CoeDeleteView, CoeUpdateView, CoeCreateView, CoeDetailView
from client.models import Coe

urlpatterns = patterns(
    '',
    url("^add/(?P<client>\d+)/$",
        permission_required("client.add_coe")(CoeCreateView.as_view()), name="coe.add"),
    url("^mod/(?P<coe>\d+)/$",
        permission_required("client.change_coe")(CoeUpdateView.as_view()), name="coe.change"),
    url("^del/(?P<client>\d+)/(?P<coe>\d+)/$",
        permission_required("client.delete_coe")(CoeDeleteView.as_view()), name="coe.delete"),
    url(r'^details/(?P<coe>\d+)/$', login_required(CoeDetailView.as_view()), name="coe.details"),


    url(r'^file/upload/$', 'client.coe.views.upload', name='document.upload'),
    url(r'^file/delete/(?P<document>\d+)$', 'client.coe.views.delete', name='document.delete'),

    url(r'^invoice/', 'client.coe.views.generate_invoice'),
)