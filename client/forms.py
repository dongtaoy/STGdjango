__author__ = 'dongtaoy'
from django.forms import ModelForm
from client.models import Visa, Stage


class VisaForm(ModelForm):
    class Meta:
        model = Visa
        fields = '__all__'

class StageForm(ModelForm):
    class Meta:
        model = Stage
        fields = '__all__'