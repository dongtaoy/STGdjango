__author__ = 'dongtaoy'
from django.views.generic.edit import UpdateView, DeleteView

from django.contrib.formtools.wizard.views import SessionWizardView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.contrib import messages
from hr.forms import EmployeeForm
from hr.models import Employee
from django.db.transaction import atomic
from django.contrib.auth.forms import UserCreationForm


# class EmployeeCreateView(SuccessMessageMixin, CreateView):
# form_class = Group
#     template_name = 'hr/employee/employee.edit.html'
#     success_url = '/hr/employee/'

FORMS = [("account", UserCreationForm),
         ("personal", EmployeeForm)]

TEMPLATES = {"account": "hr/employee/employee.account.wizard.html",
             "personal": "hr/employee/employee.personal.wizard.html"}


class EmployeeWizard(SessionWizardView):
    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        with atomic():
            employee = form_list[1]
            employee.user = form_list[0].save()
            employee.save()
        messages.success(self.request, ("%s Employee Created" % employee.name))
        return redirect('/hr/employee/')


class EmployeeUpdateView(SuccessMessageMixin, UpdateView):
    form_class = EmployeeForm
    template_name = 'hr/employee/employee.edit.html'
    success_url = '/hr/employee/'
    context_object_name = 'spec_employee'
    pk_url_kwarg = 'employee'
    model = Employee
    success_message = '%(name)s Employee updated'


class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'common/delete.confirmation.html'
    success_url = '/hr/employee/'
    pk_url_kwarg = 'employee'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        user = self.object.user
        with atomic():
            self.object.delete()
            user.delete()
        messages.success(self.request, 'Employee deleted')
        return redirect(self.get_success_url())
