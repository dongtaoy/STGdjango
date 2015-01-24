from django.contrib.auth.models import Group, Permission
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db import transaction
from django.db.transaction import atomic
from django.shortcuts import redirect
from django.views.generic import CreateView, UpdateView, DeleteView
from hr.forms import DepartmentForm, GroupCreationForm
from hr.models import Department


class DepartmentCreateView(SuccessMessageMixin, CreateView):
    form_class = DepartmentForm
    second_form_class = GroupCreationForm
    template_name = "hr/department/department.edit.html"
    success_message = "Department created"
    success_url = "/hr/department"

    def get_context_data(self, **kwargs):
        context = super(DepartmentCreateView, self).get_context_data(**kwargs)
        context["group"] = GroupCreationForm()
        context["department"] = DepartmentForm()
        return context

    def form_valid(self, form):
        with transaction.atomic():
            group = Group.objects.create(name=self.request.POST.get('name'))
            data = dict(self.request.POST.iterlists())
            if data['name']:
                group.name = self.request.POST['name']
            if 'permissions' in data.keys():
                perms = []
                for i in data["permissions"]:
                    perms.append(Permission.objects.get(id=i))
                group.permissions = perms
            else:
                group.permissions = ""
            department = DepartmentForm(self.request.POST).save(commit=False)
            department.group = group
            department.save()
        messages.success(self.request, self.success_message)
        return redirect(self.success_url)


class DepartmentUpdateView(SuccessMessageMixin, UpdateView):
    form_class = DepartmentForm
    second_form_class = GroupCreationForm
    model = Department
    template_name = "hr/department/department.edit.html"
    pk_url_kwarg = "department"
    context_object_name = "spec_department"
    success_url = "/hr/department"

    def get_success_message(self, cleaned_data):
        department = Department.objects.get(id=self.kwargs["department"])
        message = "%s Department updated" % department.group.name
        return message

    def get_context_data(self, **kwargs):
        context = super(DepartmentUpdateView, self).get_context_data(**kwargs)
        group = Group.objects.get(name=context['spec_department'])
        department = context["spec_department"]
        if 'department' not in context:
            context['department'] = self.form_class(
                initial={'label': department.label, 'description': department.description})
        if 'group' not in context:
            context['group'] = self.second_form_class(
                initial={'name': group.name, "permissions": group.permissions.all()})
        return context

    def post(self, request, *args, **kwargs):
        post = super(DepartmentUpdateView, self).post(self, request, *args, **kwargs)
        data = dict(request.POST.iterlists())
        context = self.get_context_data()
        group = Group.objects.get(name=context['spec_department'])
        if data['name']:
            group.name = request.POST['name']
        if 'permissions' in data.keys():
            perms = []
            for i in data["permissions"]:
                perms.append(Permission.objects.get(id=i))
            group.permissions = perms
        else:
            group.permissions = ""
        group.save()
        return post


class DepartmentDeleteView(DeleteView):
    model = Department
    pk_url_kwarg = "department"
    success_url = "/hr/department"
    template_name = "common/delete.confirmation.html"

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        with atomic():
            self.object.delete()
            Group.delete(self.object.group)
        messages.success(self.request, 'Department deleted')
        return redirect(self.get_success_url())