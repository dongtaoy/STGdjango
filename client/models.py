from django.db import models


# class Client(models.Model):
# pass


class Visa(models.Model):
    subClass = models.IntegerField(max_length=3)
    description = models.TextField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return str(self.subClass)


class Stage(models.Model):
    order = models.IntegerField(max_length=10)
    title = models.CharField(max_length=50)
    description = models.TextField()

    def __unicode__(self):
        return "Stage %d - %s" % self.order, self.title


        # class StageDocuments(models.Model):
        # stage = models.ForeignKey(Stage)
        #     title = models.CharField(max_length=100, null=True, blank=False)
        #     path = models.CharField(max_length=150, null=True, blank=False)
        #
        #     def __unicode__(self):
        #         return self.title