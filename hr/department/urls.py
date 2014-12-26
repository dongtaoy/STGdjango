__author__ = 'dongtaoy'
from django.conf.urls import patterns, url
from django.views.generic import ListView
from django.contrib.auth.decorators import permission_required, login_required
from hr.models import Department
from hr.department.views import DepartmentCreateView, DepartmentUpdateView, DepartmentDeleteView, GroupCreateView

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'dongtaoy_oa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$','dongtaoy_oa.crm.views.customer_index'),

    url(r'^$', login_required(ListView.as_view(
        model=Department,
        context_object_name='departments',
        template_name='hr/department/department.list.html')), name='department.list'),

    url(r'^add/$',
        permission_required('hr.add_department')(DepartmentCreateView.as_view()), name='department.add'),

    url(r'^mod/(?P<department>\d+)/$',
        permission_required('hr.change_department')(DepartmentUpdateView.as_view()), name='department.mod'),

    url(r'^del/(?P<department>\d+)/$',
        permission_required('hr.change_department')(DepartmentDeleteView.as_view()), name='department.delete'),
)
