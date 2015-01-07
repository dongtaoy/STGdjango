from django.conf.urls import patterns, include, url
from django.contrib import admin
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

admin.autodiscover()