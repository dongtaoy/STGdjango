from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'STGdjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url('^label/', include('system.label.urls')),

    url('^sidebar/', include('system.sidebar.urls')),

    url(r'^password/', include('system.password.urls')),

    url(r'^icon/', include('system.icon.urls')),

    url(r'^calendarevent/', include('system.calendarevent.urls')),
)
