from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from client.forms import PaymentForm
from client.models import Payment, Coe, Client


class PaymentCreateView(SuccessMessageMixin, CreateView):
    form_class = PaymentForm
    template_name = "client/payment/payment.edit.html"

    def get_success_message(self, cleaned_data):
        name = cleaned_data["coe"]
        return "%s's Payment updated" % name

    def get_success_url(self):
        return "/client/coe/details/%d" % int(self.kwargs["coe"])

    def get_initial(self):
        return {
            "coe": Coe.objects.get(id=self.kwargs["coe"])}


class PaymentUpdateView(SuccessMessageMixin, UpdateView):
    form_class = PaymentForm
    template_name = "client/payment/payment.edit.html"
    success_url = "/client/payment/"
    context_object_name = "spec_payment"
    pk_url_kwarg = "payment"
    model = Payment

    def get_success_message(self, cleaned_data):
        name = cleaned_data["coe"]
        return "%s's Payment updated" % name

    def get_success_url(self):
        return "/client/coe/details/%d" % int(self.kwargs["coe"])

    def get_context_data(self, **kwargs):
        context = super(PaymentUpdateView, self).get_context_data(**kwargs)
        coe = Coe.objects.get(id=self.kwargs["coe"])
        context["client"] = coe.client
        context["coe"] = coe
        return context


class PaymentDeleteView(DeleteView):
    model = Payment
    template_name = "common/delete.confirmation.html"
    pk_url_kwarg = "payment"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "payment deleted")
        return super(PaymentDeleteView, self).delete(self, request, *args, **kwargs)

    def get_success_url(self):
        coe = Coe.objects.get(id=self.kwargs["coe"])
        return "/client/coe/details/%d" % coe.id
