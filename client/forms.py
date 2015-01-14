__author__ = 'dongtaoy'
from django.forms import ModelForm
from django import forms
from client.models import Visa, Stage, Client, Institution, Coe, Payment, Document, Invoice


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
        }

    def __init__(self, *args, **kwargs):
        super(CoeForm, self).__init__(*args, **kwargs)
        self.fields['start'].widget.attrs['class'] = 'datepicker'
        self.fields['end'].widget.attrs['class'] = 'datepicker'


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
        }

        widgets = {
            "coe": forms.HiddenInput()
        }

    def __init__(self, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)
        self.fields['nextDueDate'].widget.attrs['class'] = 'datepicker'
        self.fields['receivedDate'].widget.attrs['class'] = 'datepicker'
        self.fields['paidDate'].widget.attrs['class'] = 'datepicker'


class DocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = "__all__"


class InvoiceForm(ModelForm):
    class Meta:
        model = Invoice
        fields = "__all__"
        widgets = {
            "coe": forms.HiddenInput(),
            "employee": forms.HiddenInput()
        }

    def __init__(self, *args, **kwargs):
        super(InvoiceForm, self).__init__(*args, **kwargs)
        self.fields['issueDate'].widget.attrs['class'] = 'datepicker'





