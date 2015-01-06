from django.conf.urls import patterns, url
from django.views.generic import ListView
from django.contrib.auth.decorators import permission_required, login_required
from client.models import Payment
from client.payment.views import PaymentCreateView, PaymentUpdateView, PaymentDeleteView

urlpatterns = patterns(
    '',
    url(r'^$', login_required(ListView.as_view(
        model = Payment,
        context_object_name= "payments",
        template_name="client/payment/payment.list.html")), name="payment.list"),

    url(r'^add/(?P<coe>\d+)/$',
        permission_required('client.add_payment')(PaymentCreateView.as_view()), name="payment.add"),

    url(r'^mod/(?P<client>\d+)/(?P<payment>\d+)/$',
        permission_required('client.change_payment')(PaymentUpdateView.as_view()), name="payment.edit"),

    url(r'^del/(?P<client>\d+)/(?P<payment>\d+)/$',
        permission_required('client.delete_payment')(PaymentDeleteView.as_view()), name="payment.delete"),

)