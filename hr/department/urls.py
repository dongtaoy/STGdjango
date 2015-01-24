from hr.department.views import DepartmentCreateView, DepartmentUpdateView, DepartmentDeleteView
from hr.models import Department

__author__ = 'georgecai904'
from django.conf.urls import patterns, url
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = patterns('',
    url("^$", login_required(ListView.as_view(
        template_name="hr/department/department.list.html",
        model=Department,
        context_object_name="departments"
    )), name="department.list"),

    url("^add/$",
        permission_required("hr.add_department")(DepartmentCreateView.as_view()), name="department.add"),
    url("^mod/(?P<department>\d+)/$",
        permission_required("hr.change_department")(DepartmentUpdateView.as_view()), name="department.mod"),
    url("^del/(?P<department>\d+)/$",
        permission_required("hr.delete_department")(DepartmentDeleteView.as_view()), name="department.delete"),
)