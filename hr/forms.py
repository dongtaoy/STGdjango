from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
__author__ = 'georgecai904'
from django.forms import ModelForm
from hr.models import Department, Employee
from django import forms


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


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = "__all__"


class UserCreationFormWithGroup(UserCreationForm):
    groups = forms.ModelMultipleChoiceField(queryset=Group.objects.all(), required=False)

    def save(self, commit=True):
        user = super(UserCreationFormWithGroup, self).save(commit)
        user.groups = self.cleaned_data["groups"]
        user.save()
        return user
