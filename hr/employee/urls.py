__author__ = 'dongtaoy'
from django.conf.urls import patterns, url
from django.views.generic import ListView
from django.contrib.auth.decorators import permission_required, login_required
from hr.models import Employee
from hr.employee.views import EmployeeWizard, FORMS, EmployeeUpdateView, EmployeeDeleteView

urlpatterns = patterns(
    '',

    url(r'^$', login_required(ListView.as_view(
        model=Employee,
        context_object_name='employees',
        template_name='hr/employee/employee.list.html'
    )), name='employee.list'),

    url(r'^add/$', EmployeeWizard.as_view(FORMS), name='employee.add'),

    url(r'^mod/(?P<employee>\d+)/$',
        permission_required('hr.change_employee')(EmployeeUpdateView.as_view()), name='employee.mod'),

    url(r'^del/(?P<employee>\d+)/$',
        permission_required('hr.delete_employee')(EmployeeDeleteView.as_view()), name='employee.delete'),
)
