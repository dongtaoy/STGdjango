__author__ = 'dongtaoy'
from django.forms import ModelForm
from client.models import Visa


class VisaForm(ModelForm):
    class Meta:
        model = Visa
        fields = '__all__'
