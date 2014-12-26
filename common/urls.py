from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'STGdjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # login
    url(r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'common/login.html'}),

    # logout
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login'),

    # dashboard
    url(r'^$', login_required(TemplateView.as_view(template_name='dashboard.html')), name='dashboard'),
    # url(r'^delconfirm/$', login_required(TemplateView.as_view(template_name='common/delete.confirmation.html')), name='delete.confirmation'),
)
