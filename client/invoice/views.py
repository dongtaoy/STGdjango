from django.shortcuts import redirect
from django.core.urlresolvers import reverse
import os
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from STGdjango import settings
from client.forms import InvoiceForm
from client.models import Invoice, Coe, Payment


class InvoiceCreateView(SuccessMessageMixin, CreateView):
    form_class = InvoiceForm
    template_name = "client/invoice/invoice.edit.html"
    success_url = "/client/invoice/"
    success_message = "Invoice created"

    def get_success_message(self, cleaned_data):
        name = cleaned_data["coe"]
        return "%s's Invoice created" % name

    def get_success_url(self):
        return reverse("coe.details", kwargs={"coe": int(self.kwargs["coe"])})

    def get_context_data(self, **kwargs):
        context = super(InvoiceCreateView, self).get_context_data(**kwargs)
        coe = Coe.objects.get(id=self.kwargs["coe"])
        context["coe"] = coe
        context["form"] = self.form_class(coe=int(self.kwargs["coe"]), user=self.request.user)
        return context


class InvoiceUpdateView(SuccessMessageMixin, UpdateView):
    form_class = InvoiceForm
    template_name = "client/invoice/invoice.edit.html"
    success_url = "/client/invoice/"
    context_object_name = "spec_invoice"
    pk_url_kwarg = "invoice"
    model = Invoice
    success_message = "Invoice updated"

    def get_success_message(self, cleaned_data):
        name = cleaned_data["coe"]
        return "%s's Invoice updated" % name

    def get_success_url(self):
        return reverse("coe.details", kwargs={"coe": int(self.kwargs["coe"])})

    def get_context_data(self, **kwargs):
        context = super(InvoiceUpdateView, self).get_context_data(**kwargs)
        coe = Coe.objects.get(id=self.kwargs["coe"])
        context["coe"] = coe
        invoice = self.get_object()
        context["form"] = self.form_class(instance=invoice, coe=int(self.kwargs["coe"]), user=self.request.user)
        return context


class InvoiceDeleteView(DeleteView):
    model = Invoice
    template_name = "common/delete.confirmation.html"
    success_url = "/client/invoice/"
    pk_url_kwarg = "invoice"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "invoice deleted")
        return super(InvoiceDeleteView, self).delete(self, request, *args, **kwargs)

    def get_success_url(self):
        return reverse("coe.details", kwargs={"coe": int(self.kwargs["coe"])})


from django import http
from django.template.loader import get_template
from django.template import Context
import ho.pisa as pisa
import cStringIO as StringIO
import cgi


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html = template.render(context)
    result = StringIO.StringIO()
    links = lambda uri, rel: os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ''))

    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), dest=result, link_callback=links)

    if not pdf.err:
        return http.HttpResponse(result.getvalue(), content_type='application/pdf')

    return http.HttpResponse('We had some errors<pre>%s</pre>' % cgi.escape(html))


def invoiceExport(request, **kwargs):
    invoice = Invoice.objects.get(id=kwargs["invoice"])
    commissionSum = 0
    for payment in invoice.payments.all():
        if payment.commssionClaimed:
            commissionSum += payment.commssionClaimed
    bonus = invoice.coe.bonus
    if bonus:
        bonusSum = commissionSum + bonus
        paymentSum = commissionSum*1.1 + bonus
    else:
        bonusSum = commissionSum
        paymentSum = commissionSum*1.1
    rate = invoice.coe.institution.commissionRate
    return render_to_pdf('client/invoice/invoice2.html', {
        'pagesize': 'A4',
        'invoice': invoice,
        "commissionSum": commissionSum,
        "bonus": bonus,
        "bonusSum": bonusSum,
        "paymentSum": paymentSum,
        "rate": rate,
    })

