from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse
from django.contrib.messages.views import SuccessMessageMixin
from client.forms import StageForm
from client.models import Stage


class StageCreateView(SuccessMessageMixin, CreateView):
    form_class = StageForm
    template_name = "client/stage/stage.edit.html"
    success_url = "/client/stage/"


class StageUpdateView(SuccessMessageMixin, UpdateView):
    form_class = StageForm
    template_name = "client/stage/stage.edit.html"
    success_url = "/client/stage/"
    context_object_name = "spec_stage"
    pk_url_kwarg = "stage"
    model = Stage


class StageDeleteView(DeleteView):
    model = Stage
    template_name = "common/delete.confirmation.html"
    success_url = "/client/stage/"
    pk_url_kwarg = "stage"

