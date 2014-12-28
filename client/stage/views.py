from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from client.forms import StageForm
from client.models import Stage


class StageCreateView(SuccessMessageMixin, CreateView):
    form_class = StageForm
    template_name = "client/stage/stage.edit.html"
    success_url = "/client/stage/"
    success_message = "%(title)s Stage created"


class StageUpdateView(SuccessMessageMixin, UpdateView):
    form_class = StageForm
    template_name = "client/stage/stage.edit.html"
    success_url = "/client/stage/"
    context_object_name = "spec_stage"
    pk_url_kwarg = "stage"
    model = Stage
    success_message = "%(title)s stage updated"


class StageDeleteView(DeleteView):
    model = Stage
    template_name = "common/delete.confirmation.html"
    success_url = "/client/stage/"
    pk_url_kwarg = "stage"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "stage deleted")
        return super(StageDeleteView, self).delete(self, request, *args, **kwargs)

