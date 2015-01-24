import json
from django.core import serializers
from django.contrib.auth.models import Group
from django.core.urlresolvers import reverse

__author__ = 'dongtaoy'
from django.views.generic.edit import UpdateView, DeleteView

from django.contrib.formtools.wizard.views import SessionWizardView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.contrib import messages
from hr.forms import EmployeeForm, UserCreationFormWithGroup, EmployeeUpdateForm
from hr.models import Employee
from django.db.transaction import atomic


# class EmployeeCreateView(SuccessMessageMixin, CreateView):
# form_class = Group
# template_name = 'hr/employee/employee.edit.html'
# success_url = '/hr/employee/'

FORMS = [("account", UserCreationFormWithGroup),
         ("personal", EmployeeForm)]

TEMPLATES = {"account": "hr/employee/employee.account.wizard.html",
             "personal": "hr/employee/employee.personal.wizard.html"}


class EmployeeWizard(SessionWizardView):
    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        with atomic():
            employee = form_list[1].save(commit=False)
            employee.user = form_list[0].save()
            employee.save()
        messages.success(self.request, ("%s Employee Created" % employee.name))
        return redirect('/hr/employee/')


class EmployeeUpdateView(SuccessMessageMixin, UpdateView):
    form_class = EmployeeUpdateForm
    template_name = 'hr/employee/employee.edit.html'
    success_url = '/hr/employee/'
    context_object_name = 'spec_employee'
    pk_url_kwarg = 'employee'
    model = Employee
    success_message = '%(name)s Employee updated'

    def get_context_data(self, **kwargs):
        context = super(EmployeeUpdateView, self).get_context_data(**kwargs)
        user = context['spec_employee'].user
        employee = context["spec_employee"]

        if 'employee_form' not in context:
            serialized = serializers.serialize("json", [employee])
            initial = json.loads(serialized)[0]["fields"]
            if user.groups.all():
                initial["group"] = user.groups.all()[0]
            context['form'] = self.form_class(
                initial=initial)
        return context

    def get_success_url(self):
        # user = User.type(self.request.POST["user"])
        self.object = self.get_object()
        user = self.object.user
        group = Group.objects.get(id=int(self.request.POST["group"]))
        user.groups.clear()
        user.groups.add(group)
        return reverse("employee.list")


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
