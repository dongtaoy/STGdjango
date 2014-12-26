__author__ = 'dongtaoy'
from django.forms import ModelForm
from system.models import Label, Sidebar


class LabelForm(ModelForm):
    class Meta:
        model = Label
        fields = '__all__'


class SidebarForm(ModelForm):
    class Meta:
        model = Sidebar
        fields = '__all__'