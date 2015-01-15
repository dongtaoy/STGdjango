__author__ = 'dongtaoy'
from django.forms import ModelForm
from system.models import Label, Sidebar, Icon, CalendarEvent


class LabelForm(ModelForm):
    class Meta:
        model = Label
        fields = '__all__'


class SidebarForm(ModelForm):
    class Meta:
        model = Sidebar
        fields = '__all__'


class IconForm(ModelForm):
    class Meta:
        model = Icon
        fields = '__all__'


class CalendarEventForm(ModelForm):


    class Meta:
        model = CalendarEvent
        fields = '__all__'