__author__ = 'dongtaoy'
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.contrib import messages
from django.core import serializers
from django.contrib.messages.views import SuccessMessageMixin
from system.forms import SidebarForm
from system.models import Sidebar


class SidebarListView(ListView):
    model = Sidebar
    context_object_name = 'sidebars',
    template_name = 'system/sidebar/sidebar.list.html'

    def get_context_data(self, **kwargs):
        context = {
            'sidebarsJson': serializers.serialize('json', self.object_list)
        }
        return context


class SidebarCreateView(SuccessMessageMixin, CreateView):
    form_class = SidebarForm
    template_name = 'system/sidebar/sidebar.edit.html'
    success_url = '/system/sidebar/'
    success_message = '%(text)s Sidebar created'


class SidebarUpdateView(SuccessMessageMixin, UpdateView):
    form_class = SidebarForm
    template_name = 'system/sidebar/sidebar.edit.html'
    success_url = '/system/sidebar/'
    context_object_name = 'sidebar'
    pk_url_kwarg = 'sidebar'
    model = Sidebar
    success_message = '%(text)s Sidebar updated'


class SidebarDeleteView(DeleteView):
    model = SidebarForm
    template_name = 'common/delete.confirmation.html'
    success_url = '/system/sidebar/'
    pk_url_kwarg = 'sidebar'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Sidebar deleted')
        return super(SidebarDeleteView, self).delete(self.request, *args, **kwargs)

