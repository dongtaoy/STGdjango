from django import forms
from django.contrib.auth.models import Group

__author__ = 'georgecai904'
from django.forms import ModelForm
from hr.models import Department, Employee


class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        # fields = '__all__'
        exclude = ('group',)



# class DepartmentEditForm(ModelForm):
# class Meta:
#         model = (Department, Group)
#         fields = '__all__'


class GroupCreationForm(ModelForm):
    class Meta:
        model = Group
        fields = "__all__"

    def save(self, commit=True):
        group = super(GroupCreationForm, self).save(commit=False)
        if commit:
            group = Group.objects.create(name=self.cleaned_data["name"])
            group.permissions = self.cleaned_data["permissions"]
            group.save()
        return group


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['dob'].widget.attrs['class'] = 'datepicker'


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = "__all__"
