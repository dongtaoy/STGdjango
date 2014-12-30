from django.contrib.auth.models import Group

__author__ = 'georgecai904'
from django.contrib import messages
from django.contrib.formtools.wizard.views import SessionWizardView
from django.db.transaction import atomic
from django.shortcuts import redirect
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from hr.forms import DepartmentForm, GroupCreationForm, GroupForm
from hr.models import Department

FORMS = [
    ("group", GroupCreationForm),
    ("profile", DepartmentForm)
]

TEMPLATES = {
    "group": "hr/department/department.group.wizard.html",
    "profile": "hr/department/department.profile.wizard.html"
}


class DepartmentWizard(SessionWizardView):
    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        with atomic():
            department = form_list[1].save(commit=False)
            department.group = form_list[0].save()
            department.save()
        messages.success(self.request, ("%s Department Created" % department.group.name))
        return redirect('/hr/department/')


class DepartmentUpdateView(SuccessMessageMixin, UpdateView):
    form_class = DepartmentForm
    second_form_class = GroupForm
    template_name = 'hr/department/department.edit.html'
    success_url = '/hr/department/'
    context_object_name = 'spec_department'
    pk_url_kwarg = 'department'
    model = Department

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
        data = request.POST
        context = self.get_context_data()
        group = Group.objects.get(name=context['spec_department'])
        if data['name']:
            group.name = data['name']
        if data['permissions']:
            group.permissions = data['permissions']
        group.save()
        return post


class DepartmentDeleteView(DeleteView):
    model = Department
    template_name = 'common/delete.confirmation.html'
    success_url = '/hr/department/'
    pk_url_kwarg = 'department'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Department deleted")
        return super(DepartmentDeleteView, self).delete(self, request, *args, **kwargs)
