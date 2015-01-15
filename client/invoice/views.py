from django.core.urlresolvers import reverse
import os
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from STGdjango import settings
from client.forms import InvoiceForm
from client.models import Invoice, Coe


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

    def get_initial(self):
        coe = Coe.objects.get(id=self.kwargs["coe"])
        return {
            "coe": coe,
            "employee": self.request.user.employee}

    def get_context_data(self, **kwargs):
        context = super(InvoiceCreateView, self).get_context_data(**kwargs)
        coe = Coe.objects.get(id=self.kwargs["coe"])
        context["coe"] = coe
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


def index(request):
    return http.HttpResponse("""
        <html><body>
            <h1>Example 1</h1>
            Please enter some HTML code:
            <form action="/client/download/" method="post" enctype="multipart/form-data">
            <textarea name="data">Hello <strong>World</strong></textarea>
            <br />
            <input type="submit" value="Convert HTML to PDF" />
            </form>
            <hr>
            <h1>Example 2</h1>
            <p><a href="/client/ezpdf_sample">Example with template</a>
            <a class="btn btn-lg blue hidden-print margin-bottom-5"
                onclick="javascript:window.print();">Print<i class="fa fa-print"></i>
        </body></html>
        """)


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html = template.render(context)
    result = StringIO.StringIO()
    # pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("ISO-8859-1")), result)
    links = lambda uri, rel: os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ''))

    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), dest=result, link_callback=links)

    if not pdf.err:
        return http.HttpResponse(result.getvalue(), content_type='application/pdf')

    return http.HttpResponse('We had some errors<pre>%s</pre>' % cgi.escape(html))


def invoiceExport(request, **kwargs):
    invoice = Invoice.objects.get(id=kwargs["invoice"])
    sum = 0
    for payment in invoice.payments.all():
        if payment.commssionClaimed:
            sum += payment.commssionClaimed
    return render_to_pdf('client/invoice/invoice.html', {
        'pagesize': 'A4',
        'invoice': invoice,
        "sum": sum
    })

