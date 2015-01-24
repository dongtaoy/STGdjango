from django.conf.urls import patterns, include, url, handler403, handler404, handler500
from django.contrib import admin
from django.views.generic import TemplateView
import settings


urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'STGdjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # Common urls
    url(r'^', include('common.urls')),

    # system urls
    url(r'^system/', include('system.urls')),

    # client urls
    url(r'^client/', include('client.urls')),

    # Admin urls
    url(r'^admin/', include(admin.site.urls)),

    # hr urls
    url(r'^hr/', include('hr.urls')),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^500/$', "common.views.handler500"),
        (r'^404/$', "common.views.handler404"),
    )


handler500 = "common.views.handler500"
handler404 = "common.views.handler404"


admin.autodiscover()
