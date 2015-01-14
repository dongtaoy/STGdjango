from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'STGdjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'django.contrib.auth.views.password_change',
        {'template_name': 'system/password/password.change.html',
         'post_change_redirect': '/'}, name="password.reset"),
)
