__author__ = 'dongtaoy'
from django.contrib import admin
from hr.models import Employee, Department
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User, Group


# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = 'employees'


# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (EmployeeInline, )


class DepartmentInline(admin.StackedInline):
    model = Department
    can_delete = False
    verbose_name_plural = 'departments'


class GroupAdmin(GroupAdmin):
    inlines = (DepartmentInline, )


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
admin.site.register(Group, GroupAdmin)


