__author__ = 'dongtaoy'
from django.forms import ModelForm
from client.models import Visa, Stage, Client, Institution, Coe, Payment, Document


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
        fields = "__all__"

        labels = {
            'totalTuitionFee': "Total Tuition Fee",
            "referalCommission": "Referal's Commission",
            "consultantCommission": "Consultant's Commission",
        }

        # def __init__(self):
        # super(CoeForm, self).__init__(ModelForm)
        # self.fields['client'].widget.attrs['readonly'] = True


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


class DocumentForm(ModelForm):
    class Meta:
        model = Document

