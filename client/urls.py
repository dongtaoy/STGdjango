from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import ListView, DetailView
from client.coe.views import CoeCreateView, CoeUpdateView, CoeDeleteView
from client.models import Client
from client.views import ClientCreateView, ClientUpdateView, ClientDeleteView, ClientDetailView

urlpatterns = patterns('',

    url(r'^$', login_required(ListView.as_view(
            model=Client,
            context_object_name="clients",
            template_name="client/client.list.html")), name="client.list"),

    url(r'^add/$',
        permission_required("client.add_client")(ClientCreateView.as_view()), name="client.add"),
    url(r'^mod/(?P<section>\w+)/(?P<client>\d+)/$',
        permission_required("client.change_client")(ClientUpdateView.as_view()), name="client.edit"),
    url(r'^del/(?P<client>\d+)/$',
        permission_required("client.delete_client")(ClientDeleteView.as_view()), name="client.delete"),
    url(r'^details/(?P<client>\d+)/$', login_required(ClientDetailView.as_view()), name="client.details"),

    url(r'^visa/', include("client.visa.urls")),
    url(r'^stage/', include("client.stage.urls")),
    url(r'^institution/', include('client.institution.urls')),
    url(r'^coe/', include('client.coe.urls')),
    url(r"^payment/", include("client.payment.urls")),
)
