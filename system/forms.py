__author__ = 'dongtaoy'
from django.forms import ModelForm
from system.models import Label, Sidebar, Glyphicon


class LabelForm(ModelForm):
    class Meta:
        model = Label
        fields = '__all__'


class SidebarForm(ModelForm):
    class Meta:
        model = Sidebar
        fields = '__all__'


class GlyphiconForm(ModelForm):
    class Meta:
        model = Glyphicon
        fields = '__all__'