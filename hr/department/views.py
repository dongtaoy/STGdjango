from django.contrib import messages
from django.contrib.formtools.wizard.views import SessionWizardView
from django.db.transaction import atomic
from django.shortcuts import redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.admin import Group
from django.contrib.messages.views import SuccessMessageMixin
from hr.forms import DepartmentForm, GroupCreationForm
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
