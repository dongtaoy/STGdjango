from django.conf.urls import patterns, url
from django.views.generic import ListView
from django.contrib.auth.decorators import permission_required, login_required
from client.models import Invoice
from client.invoice.views import InvoiceCreateView, InvoiceUpdateView, InvoiceDeleteView


urlpatterns = patterns(
    '',
    url(r'^$', login_required(ListView.as_view(
        model=Invoice,
        context_object_name="invoices",
        template_name="client/invoice/invoice.list.html")), name="invoice.list"),

    # url(r"^$", login_required(InvoiceListView.as_view()), name="invoice.dueDate"),

    url(r'^add/(?P<coe>\d+)/$',
        permission_required('client.add_invoice')(InvoiceCreateView.as_view()), name="invoice.add"),

    url(r'^mod/(?P<coe>\d+)/(?P<invoice>\d+)/$',
        permission_required('client.change_invoice')(InvoiceUpdateView.as_view()), name="invoice.edit"),

    url(r'^del/(?P<coe>\d+)/(?P<invoice>\d+)/$',
        permission_required('client.delete_invoice')(InvoiceDeleteView.as_view()), name="invoice.delete"),

    url(r"^export/(?P<invoice>\d+)/invoice.pdf", "client.invoice.views.invoiceExport", name="invoice.export")
    # url(r'^add/$',
    #     permission_required('client.add_invoice')(InvoiceCreateView.as_view()), name="invoice.add"),
    #
    # url(r'^mod/(?P<invoice>\d+)/$',
    #     permission_required('client.change_invoice')(InvoiceUpdateView.as_view()), name="invoice.edit"),
    #
    # url(r'^del/(?P<invoice>\d+)/$',
    #     permission_required('client.delete_invoice')(InvoiceDeleteView.as_view()), name="invoice.delete"),
)