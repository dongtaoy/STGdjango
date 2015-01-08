from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.forms import ModelForm
from django.shortcuts import render_to_response
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.views.generic import ListView
from client.models import Payment
import datetime
from client.models import Client, Coe, Payment, Stage


def get_custom_form(customModel, customFields):
    class _customForm(ModelForm):
        class Meta:
            model = customModel
            fields = customFields

    return _customForm


CLIENT_FIELDS = {
    "personal": ("name", "preferredName", "dob", "phone", "email", "nationality", "onshore"),
    "visa": ("visa", "expire"),
    "service": (
        "status", "referal", "consultant", "clientManager", "serviceFee", "thirdPartyFeeReceived",
        "thirdPartyFeePaid"),
    "notes": ("note",)
}

MODELS = {
    "client": Client,
}


class ClientCreateView(SuccessMessageMixin, CreateView):
    form_class = get_custom_form(MODELS['client'], CLIENT_FIELDS["personal"])
    success_url = "/client/"
    template_name = "client/client.edit.html"
    success_message = "%(name)s Client created"


class ClientUpdateView(SuccessMessageMixin, UpdateView):
    template_name = "client/client.edit.html"

    context_object_name = "spec_client"
    pk_url_kwarg = "client"
    model = Client

    def get_form(self, form_class):
        custom_form = get_custom_form(MODELS['client'], CLIENT_FIELDS[self.kwargs["section"]])
        form = super(ClientUpdateView, self).get_form(custom_form)
        return form

    def get_success_url(self):
        id = self.kwargs["client"]
        return "/client/details/" + id

    def get_success_message(self, cleaned_data):
        print cleaned_data
        return "Client %s information updated" % (self.kwargs["section"])

    def get_context_data(self, **kwargs):
        context = super(ClientUpdateView, self).get_context_data(**kwargs)
        context['section'] = self.kwargs["section"]
        return context


class ClientDeleteView(DeleteView):
    model = Client
    template_name = "common/delete.confirmation.html"
    success_url = "/client/"
    pk_url_kwarg = "client"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Client deleted")
        return super(ClientDeleteView, self).delete(self, request, *args, **kwargs)


class ClientDetailView(DetailView):
    model = Client
    template_name = "client/client.info.html"
    pk_url_kwarg = "client"

    # def get_context_data(self, **kwargs):
    # context = super(ClientDetailView, self).get_context_data(**kwargs)
    # context["stages"] = Stage.objects.all()
    #     return context


def uploadtest(request):
    return render_to_response('client/client.upload.html')


