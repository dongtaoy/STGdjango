__author__ = 'zhangjingyuan'
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from system.forms import GlyphiconForm
from system.models import Glyphicon


class GlyphiconCreateView(SuccessMessageMixin, CreateView):
    form_class = GlyphiconForm
    template_name = '/system/glyphicon/glyphicon.edit.html'
    success_url = '/system/glyphicon/'
    success_message = '%(name)s Glyphicon created'


class GlyphiconUpdateView(SuccessMessageMixin, UpdateView):
    form_class = GlyphiconForm
    template_name = '/system/glyphicon/glyphicon.edit.html'
    success_url = '/system/glyphicon/'
    success_message = '%(name)s Glyphicon updated'
    context_object_name = 'spec_glyphicon'
    pk_url_kwarg = 'glyphicon'
    model = Glyphicon



class GlyphiconDeleteView(DeleteView):
    template_name = 'common/delete.confirmation.html'
    model = Glyphicon
    success_url = '/system/glyphicon/'
    pk_url_kwarg = 'glyphicon'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Glyphicon deleted')
        return super(GlyphiconDeleteView, self).delete(self.request, *args, **kwargs)
