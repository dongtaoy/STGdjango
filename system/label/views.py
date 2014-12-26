__author__ = 'dongtaoy'
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from system.forms import LabelForm
from system.models import Label


class LabelCreateView(SuccessMessageMixin, CreateView):
    form_class = LabelForm
    template_name = 'system/label/label.edit.html'
    success_url = '/system/label/'
    success_message = '%(name)s Label created'


class LabelUpdateView(SuccessMessageMixin, UpdateView):
    form_class = LabelForm
    template_name = 'system/label/label.edit.html'
    success_url = '/system/label/'
    context_object_name = 'spec_label'
    pk_url_kwarg = 'label'
    model = Label
    success_message = '%(name)s Label updated'


class LabelDeleteView(DeleteView):
    model = Label
    template_name = 'common/delete.confirmation.html'
    success_url = '/system/label/'
    pk_url_kwarg = 'label'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Label deleted')
        return super(LabelDeleteView, self).delete(self.request, *args, **kwargs)

