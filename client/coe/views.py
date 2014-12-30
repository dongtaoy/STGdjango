from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from client.forms import CoeForm
from client.models import Coe, Client


class CoeCreateView(SuccessMessageMixin, CreateView):
    form_class = CoeForm
    template_name = "client/coe/coe.edit.html"
    success_message = "new COE created"

    def get_success_url(self):
        return "/client/details/%d" % int(self.request.POST["client"])

    def get_success_message(self, cleaned_data):
        id = int(self.request.POST["client"])
        client = Client.objects.get(id=id)
        return "%s's COE created" % client.name

    def get_initial(self):
        return {
            "client": Client.objects.get(id=self.kwargs["client"])}


class CoeUpdateView(SuccessMessageMixin, UpdateView):
    form_class = CoeForm
    model = Coe
    pk_url_kwarg = "coe"
    template_name = "client/coe/coe.edit.html"
    context_object_name = "spec_coe"

    def get_success_url(self):
        print self.request.POST["client"]
        return "/client/details/%d" % int(self.request.POST["client"])


    def get_context_data(self, **kwargs):
        context = super(CoeUpdateView, self).get_context_data(**kwargs)
        context["client"] = Client.objects.get(id=self.kwargs["client"])
        return context

    def get_success_message(self, cleaned_data):
        id = int(self.request.POST["client"])
        client = Client.objects.get(id=id)
        return "%s's COE updated" % client.name


class CoeDeleteView(DeleteView):
    model = Coe
    template_name = "common/delete.confirmation.html"
    pk_url_kwarg = "coe"
    # success_url = "/client"

    def get_success_url(self):
        return "/client/details/%d" % int(self.kwargs["client"])

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "COE deleted")
        return super(CoeDeleteView, self).delete(self, request, *args, **kwargs)




