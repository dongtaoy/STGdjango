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

handler404 = TemplateView.as_view(template_name="common/404.html")
handler500 = TemplateView.as_view(template_name="common/500.html")
handler403 = TemplateView.as_view(template_name="common/403.html")

admin.autodiscover()