__author__ = 'dongtaoy'
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse
from django.contrib.auth.admin import Group
from django.contrib.messages.views import SuccessMessageMixin
from hr.forms import DepartmentForm
from hr.models import Department

class GroupCreateView(SuccessMessageMixin, CreateView):
    form_class = Group
    template_name = 'hr/department/department.edit.html'
    success_url = '/hr/department'

class DepartmentCreateView(SuccessMessageMixin, CreateView):
    form_class = DepartmentForm
    template_name = 'hr/department/department.edit.html'
    success_url = '/hr/department/'


class DepartmentUpdateView(SuccessMessageMixin, UpdateView):
    form_class = DepartmentForm
    template_name = 'hr/department/department.edit.html'
    success_url = '/hr/department/'
    context_object_name = 'spec_department'
    pk_url_kwarg = 'department'
    model = Department


class DepartmentDeleteView(DeleteView):
    model = Department
    template_name = 'common/delete.confirmation.html'
    success_url = '/hr/department/'
    pk_url_kwarg = 'department'
