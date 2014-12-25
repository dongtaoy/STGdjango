__author__ = 'dongtaoy'
from django.db import models


class Employee(models.Model):
    phone = models.CharField(max_length=45, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    user = models.OneToOneField('auth.User')

    class Meta:
        permissions = (('change_own_password', 'Can change own password'),)

    def __unicode__(self):
        return self.user.last_name + self.user.first_name

    def full_name(self):
        return self.user.last_name + self.user.first_name


class Department(models.Model):
    leader = models.ForeignKey('hr.Employee', blank=True, null=True)
    label = models.ForeignKey('system.Label', blank=True, null=True, default=None, on_delete=models.SET_NULL)
    group = models.OneToOneField('auth.Group')
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.group.name
