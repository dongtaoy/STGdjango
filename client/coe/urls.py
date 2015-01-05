from django.conf.urls import patterns, url
from django.views.generic import ListView
from django.contrib.auth.decorators import permission_required, login_required
from client.coe.views import CoeDeleteView, CoeUpdateView, CoeCreateView
from client.models import Coe

urlpatterns = patterns(
    '',
    url("^add/(?P<client>\d+)/$",
        permission_required("client.add_coe")(CoeCreateView.as_view()), name="coe.add"),
    url("^mod/(?P<client>\d+)/(?P<coe>\d+)/$",
        permission_required("client.change_coe")(CoeUpdateView.as_view()), name="coe.change"),
    url("^del/(?P<client>\d+)/(?P<coe>\d+)/$",
        permission_required("client.delete_coe")(CoeDeleteView.as_view()), name="coe.delete"),
)