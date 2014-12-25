__author__ = 'dongtaoy'
from django.conf.urls import patterns, url
from django.views.generic import ListView
from django.contrib.auth.decorators import permission_required, login_required
from system.models import Label

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'dongtaoy_oa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$','dongtaoy_oa.crm.views.customer_index'),

    url(r'^$', login_required(ListView.as_view(
        model=Label,
        context_object_name='labels',
        template_name='system/label/label.list.html')), name='label.list'),


)
