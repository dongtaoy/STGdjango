__author__ = 'dongtaoy'
from django.db import models


class Label(models.Model):
    name = models.CharField(max_length=50)
    css = models.CharField(max_length=50, null=True, blank=True)

    def __unicode__(self):
        return self.name


class Icon(models.Model):
    name = models.CharField(max_length=50)
    css = models.CharField(max_length=50, null=True, blank=True)

    def __unicode__(self):
        return self.name


class Sidebar(models.Model):
    text = models.CharField(max_length=45, blank=True)
    url = models.CharField(max_length=100, blank=True)
    order = models.IntegerField(max_length=10, blank=True, null=True)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children')
    icon = models.ForeignKey(Icon, blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['order']

    def __unicode__(self):
        return self.text



