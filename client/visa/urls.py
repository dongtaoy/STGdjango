__author__ = 'dongtaoy'
from django.conf.urls import patterns, url
from django.views.generic import ListView
from django.contrib.auth.decorators import permission_required, login_required
from client.models import Visa
from client.visa.views import VisaCreateView, VisaUpdateView, VisaDeleteView

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'dongtaoy_oa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$','dongtaoy_oa.crm.views.customer_index'),

    url(r'^$', login_required(ListView.as_view(
        model=Visa,
        context_object_name='visas',
        template_name='client/visa/visa.list.html')), name='visa.list'),

    url(r'^add/$',
        permission_required('client.add_visa')(VisaCreateView.as_view()), name='visa.add'),

    url(r'^mod/(?P<visa>\d+)/$',
        permission_required('client.change_visa')(VisaUpdateView.as_view()), name='visa.mod'),

    url(r'^del/(?P<visa>\d+)/$',
        permission_required('client.change_visa')(VisaDeleteView.as_view()), name='visa.delete'),
)
