__author__ = 'dongtaoy'
from django.conf.urls import patterns, url
from django.views.generic import ListView
from django.contrib.auth.decorators import permission_required, login_required
from system.models import Label
from system.label.views import LabelCreateView, LabelUpdateView

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

    url(r'^add/$',
        permission_required('system.add_label')(LabelCreateView.as_view()), name='label.add'),

    url(r'^mod/(?P<label>\d+)/$',
        permission_required('system.change_label')(LabelUpdateView.as_view()), name='label.mod'),


)
