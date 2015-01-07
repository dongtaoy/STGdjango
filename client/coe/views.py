from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.messages.views import SuccessMessageMixin
from client.forms import CoeForm, DocumentForm
from client.models import Coe, Client, Stage, Document
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.core.urlresolvers import reverse



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
        return "/client/coe/details/%d" % int(self.kwargs["coe"])

    def get_context_data(self, **kwargs):
        context = super(CoeUpdateView, self).get_context_data(**kwargs)
        coe = Coe.objects.get(id=self.kwargs["coe"])
        context["client"] = coe.client
        return context

    def get_success_message(self, cleaned_data):
        coe = Coe.objects.get(id=self.kwargs["coe"])
        name = coe.client.name
        return "%s's COE updated" % name


class CoeDeleteView(DeleteView):
    model = Coe
    template_name = "common/delete.confirmation.html"
    pk_url_kwarg = "coe"
    # success_url = "/client"

    def get_success_url(self):
        coe = Coe.objects.get(id=self.kwargs["coe"])
        return "/client/details/%d" % coe.client.id

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "COE deleted")
        return super(CoeDeleteView, self).delete(self, request, *args, **kwargs)


class CoeDetailView(DetailView):
    model = Coe
    template_name = "client/coe/coe.details.html"
    pk_url_kwarg = "coe"

    def get_context_data(self, **kwargs):
        context = super(CoeDetailView, self).get_context_data(**kwargs)
        coe = context["coe"]
        context["client"] = coe.client
        context["stages"] = Stage.objects.all()
        return context


def upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.title = document.file.name
            document.save()
            return HttpResponse()
    return HttpResponse()


def delete(request, document):
    document = Document.objects.get(id=document)
    coe = document.coe
    document.file.delete()
    document.delete()
    return redirect(reverse("coe.details", kwargs={"coe": coe.id}) + "#tab_3")