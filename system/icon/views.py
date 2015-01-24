__author__ = 'zhangjingyuan'
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from system.forms import IconForm
from system.models import Icon


class IconCreateView(SuccessMessageMixin, CreateView):
    form_class = IconForm
    template_name = 'system/icon/icon.edit.html'
    success_url = '/system/icon/'
    success_message = '%(name)s Icon created'


class IconUpdateView(SuccessMessageMixin, UpdateView):
    form_class = IconForm
    template_name = 'system/icon/icon.edit.html'
    success_url = '/system/icon/'
    success_message = '%(name)s Icon updated'
    context_object_name = 'spec_icon'
    pk_url_kwarg = 'icon'
    model = Icon


class IconDeleteView(DeleteView):
    template_name = 'common/delete.confirmation.html'
    model = Icon
    success_url = '/system/icon/'
    pk_url_kwarg = 'icon'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Icon deleted')
        return super(IconDeleteView, self).delete(self.request, *args, **kwargs)
