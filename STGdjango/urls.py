from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'STGdjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # Common urls
    url(r'^', include('common.urls')),

    # system urls
    url(r'^system/', include('system.urls')),

    # Admin urls
    url(r'^admin/', include(admin.site.urls)),
)

admin.autodiscover()