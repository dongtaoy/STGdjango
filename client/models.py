from django.db import models


class Client(models.Model):
    pass


class Visa(models.Model):
    subClass = models.IntegerField(max_length=3)
    description = models.TextField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return str(self.subClass)


class Stage(models.Model):
    client = models.ForeignKey(Client)
    order = models.IntegerField(max_length=2, null=True, blank=False)
    title = models.CharField(max_length=50, null=True, blank=False)
    description = models.TextField()

    def __unicode__(self):
        return "Stage "+str(self.number)+"-"+self.title


class StageDocuments(models.Model):
    stage = models.ForeignKey(Stage)
    title = models.CharField(max_length=100, null=True, blank=False)
    path = models.CharField(max_length=150, null=True, blank=False)

    def __unicode__(self):
        return self.title