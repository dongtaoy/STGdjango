__author__ = 'dongtaoy'
from django.forms import ModelForm
from system.models import Label


class LabelForm(ModelForm):
    class Meta:
        model = Label
        fields = '__all__'

