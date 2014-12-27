__author__ = 'dongtaoy'
from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=50, default=None, null=True)
    phone = models.CharField(max_length=45, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    email = models.EmailField(default=None, null=True)
    user = models.OneToOneField('auth.User')

    def __unicode__(self):
        return self.name


class Department(models.Model):
    label = models.ForeignKey('system.Label', blank=True, null=True, default=None, on_delete=models.SET_NULL)
    group = models.OneToOneField('auth.Group')
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.group.name
