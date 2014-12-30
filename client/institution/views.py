from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from client.forms import InstitutionForm
from client.models import Institution


class InstitutionCreateView(SuccessMessageMixin, CreateView):
    form_class = InstitutionForm
    template_name = "client/institution/institution.edit.html"
    success_url = "/client/institution"
    success_message = "%(name)s Institution created"


class InstitutionUpdateView(SuccessMessageMixin, UpdateView):
    form_class = InstitutionForm
    template_name = "client/institution/institution.edit.html"
    success_url = "/client/institution"
    success_message = "%(name)s Institution updated"
    model = Institution
    pk_url_kwarg = "institution"
    context_object_name = "spec_institution"


class InstitutionDeleteView(DeleteView):
    template_name = "common/delete.confirmation.html"
    success_url = "/client/institution"
    pk_url_kwarg = "institution"
    model = Institution

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Institution deleted")
        return super(InstitutionDeleteView, self).delete(self, request, *args, **kwargs)

