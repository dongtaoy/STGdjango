import datetime
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from client.forms import PaymentForm
from client.models import Payment, Coe, Institution


class PaymentCreateView(SuccessMessageMixin, CreateView):
    form_class = PaymentForm
    template_name = "client/payment/payment.edit.html"

    def get_success_message(self, cleaned_data):
        name = cleaned_data["coe"]
        return "%s's Payment created" % name

    def get_initial(self):
        return {
            "coe": Coe.objects.get(id=self.kwargs["coe"])}

    def get_context_data(self, **kwargs):
        context = super(PaymentCreateView, self).get_context_data(**kwargs)
        coe = Coe.objects.get(id=self.kwargs["coe"])
        context["coe"] = coe
        return context

    def post(self, request, *args, **kwargs):
        coe = Coe.objects.get(id=int(request.POST["coe"]))
        rate = coe.institution.commissionRate
        form = self.form_class(self.request.POST)
        if form.is_valid():
            if self.request.POST["paidAmount"] and rate:
                claimed = float(self.request.POST["paidAmount"]) * rate
                payment = form.save(commit=False)
                payment.commssionClaimed = claimed
                payment.save()
            else:
                payment = form.save(commit=True)
        return redirect(reverse("coe.details", kwargs={"coe": int(self.kwargs["coe"])}))


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
        return reverse("coe.details", kwargs={"coe": int(self.kwargs["coe"])})

    def get_context_data(self, **kwargs):
        context = super(PaymentUpdateView, self).get_context_data(**kwargs)
        coe = Coe.objects.get(id=self.kwargs["coe"])
        context["client"] = coe.client
        context["coe"] = coe
        return context

    def post(self, request, *args, **kwargs):
        super(PaymentUpdateView, self).post(request, *args, **kwargs)
        coe = self.get_object().coe
        rate = coe.institution.commissionRate
        self.object = self.get_object()
        if self.request.POST["paidAmount"] and rate:
            claimed = float(self.request.POST["paidAmount"]) * rate
            self.object.commssionClaimed = claimed
            self.object.save()
        return redirect(reverse("coe.details", kwargs={"coe": int(self.kwargs["coe"])}))


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


class PaymentListView(ListView):
    model = Payment
    template_name = "client/payment/payment.dueDate.html"
    context_object_name = "payments"

    def get_context_data(self, **kwargs):
        context = super(PaymentListView, self).get_context_data(**kwargs)
        context["now"] = datetime.datetime.now().date()
        return context
