__author__ = 'georgecai904'
from django.forms import ModelForm
from hr.models import Department


class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = '__all__'