from django.db import models


class Visa(models.Model):
    name = models.CharField(max_length='50', null=True, blank=True)
    subClass = models.IntegerField(max_length=3, null=True, blank=True)

    def __unicode__(self):
        return self.subClass + " " + self.name
