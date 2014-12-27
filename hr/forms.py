__author__ = 'georgecai904'
from django.forms import ModelForm
from hr.models import Department, Employee


class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = '__all__'


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        exclude = ('user',)