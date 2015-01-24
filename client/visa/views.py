__author__ = 'dongtaoy'
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from client.forms import VisaForm
from client.models import Visa


class VisaCreateView(SuccessMessageMixin, CreateView):
    form_class = VisaForm
    template_name = 'client/visa/visa.edit.html'
    success_url = '/client/visa/'
    success_message = "%(subClass)s Visa created"


class VisaUpdateView(SuccessMessageMixin, UpdateView):
    form_class = VisaForm
    template_name = 'client/visa/visa.edit.html'
    success_url = '/client/visa/'
    context_object_name = 'spec_visa'
    pk_url_kwarg = 'visa'
    model = Visa
    success_message = "%(subClass)s Visa updated"


class VisaDeleteView(DeleteView):
    model = Visa
    template_name = 'common/delete.confirmation.html'
    success_url = '/client/visa/'
    pk_url_kwarg = 'visa'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Visa deleted")
        return super(VisaDeleteView, self).delete(self, request, *args, **kwargs)