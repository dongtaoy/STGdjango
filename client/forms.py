from django.shortcuts import get_object_or_404

__author__ = 'dongtaoy'
from django.forms import ModelForm
from django import forms
from client.models import *


class VisaForm(ModelForm):
    class Meta:
        model = Visa
        fields = '__all__'


class StageForm(ModelForm):
    class Meta:
        model = Stage
        fields = '__all__'


class InstitutionForm(ModelForm):
    class Meta:
        model = Institution
        fields = '__all__'


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = "__all__"


def get_custom_form(customModel, customFields):
    class _customForm(ModelForm):
        class Meta:
            model = customModel
            fields = customFields
            labels = {
                "preferredName": "Preferred Name",
                "dob": "Date of Birth",
                "clientManager": "Client Manager",
                "serviceFee": "Service Fee",
                "thirdPartyFeeReceived": "Third Party Fee Received",
                "thirdPartyFeePaid": "Third Party Fee Paid"
            }

    return _customForm


class CoeForm(ModelForm):
    class Meta:
        model = Coe
        # fields = "__all__"
        exclude = ("documents", )
        labels = {
            'totalTuitionFee': "Total Tuition Fee",
            "referalCommission": "Referal's Commission",
            "consultantCommission": "Consultant's Commission",
            "coeNumber": "Coe Number",
        }
        widgets = {
            "client": forms.HiddenInput()
        }


class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = "__all__"

        labels = {
            'receivedAmount': "Received Amount",
            "receivedDate": "Received Date",
            "paidAmount": "Paid Amount",
            "paidDate": "Paid Date",
            "commssionClaimed": "Commssion Claimed",
            "commssionRecevied": "Commssion Recevied",
            "previousPayment": "Previous Payment",
        }

        widgets = {
            "coe": forms.HiddenInput(),
            "commssionClaimed": forms.HiddenInput()
        }


class DocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = "__all__"


class InvoiceForm(ModelForm):
    def __init__(self, *args, **kwargs):
        coe_id = kwargs.pop('coe', 0)
        user = kwargs.pop('user', 0)
        super(InvoiceForm, self).__init__(*args, **kwargs)
        if coe_id and user:
            coe = Coe.objects.get(id=int(coe_id))
            self.fields["coe"].initial = coe
            self.fields["employee"].initial = user.employee
            self.fields['payments'].queryset = Payment.objects.filter(coe=coe)

    class Meta:
        model = Invoice
        fields = "__all__"
        widgets = {
            "coe": forms.HiddenInput(),
            "employee": forms.HiddenInput()
        }
        labels = {
            "number": "Invoice Number",
            "issueDate": "Issue Date",
        }


