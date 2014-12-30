__author__ = 'dongtaoy'
from django.forms import ModelForm
from client.models import Visa, Stage, Client


class VisaForm(ModelForm):
    class Meta:
        model = Visa
        fields = '__all__'


class StageForm(ModelForm):
    class Meta:
        model = Stage
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


