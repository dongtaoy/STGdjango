from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'STGdjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'client.views.clientList', name="client"),
    url(r'^details/$', 'client.views.clientDetails'),
    url(r'^visa/', include("client.visa.urls")),
    url(r'^stage/', include("client.stage.urls")),

)
