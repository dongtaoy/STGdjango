from django.conf.urls import patterns, url
from django.contrib.auth.decorators import permission_required, login_required
from client.payment.views import PaymentCreateView, PaymentUpdateView, PaymentDeleteView, PaymentListView


urlpatterns = patterns(
    '',
    # url(r'^$', login_required(ListView.as_view(
    #     model=Payment,
    #     context_object_name="payments",
    #     template_name="client/payment/payment.list.html")), name="payment.list"),

    url(r"^$", login_required(PaymentListView.as_view()), name="payment.dueDate"),

    url(r'^add/(?P<coe>\d+)/$',
        permission_required('client.add_payment')(PaymentCreateView.as_view()), name="payment.add"),

    url(r'^mod/(?P<coe>\d+)/(?P<payment>\d+)/$',
        permission_required('client.change_payment')(PaymentUpdateView.as_view()), name="payment.edit"),

    url(r'^del/(?P<coe>\d+)/(?P<payment>\d+)/$',
        permission_required('client.delete_payment')(PaymentDeleteView.as_view()), name="payment.delete"),


)