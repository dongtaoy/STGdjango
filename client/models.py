from django.db import models
from hr.models import Employee


class Client(models.Model):
    # Personal Information
    name = models.CharField(max_length=100)
    preferredName = models.CharField(max_length=100, blank=True, null=True)
    DoB = models.DateField()
    nationality = models.CharField(max_length=100)
    Email = models.EmailField(blank=True, null=True)
    contactNumber = models.CharField(max_length=20, blank=True, null=True)
    onshore = models.BooleanField(blank=True, null=True)

    # Visa Information
    visa = models.ForeignKey(Visa)
    expiryDate = models.DateField(blank=True, null=True)

    # Service Information
    status = models.CharField(max_length=100)
    referal = models.ForeignKey(Employee, blank=True, null=True)
    Consultant = models.ForeignKey(Employee, blank=True, null=True)
    clientManager = models.ForeignKey(Employee, blank=True, null=True)
    stage = models.ManyToManyField(Stage)
    serviceFee = models.FloatField()
    thirdPartyFeeReceived = models.FloatField(blank=True, null=True)
    thirdPartyFeePaid = models.FloatField(blank=True, null=True)

    # Others
    note = models.TextField(blank=True, null=True)


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
        return "Stage %d - %s" % (self.order, self.title)


        # class StageDocuments(models.Model):
        # stage = models.ForeignKey(Stage)
        # title = models.CharField(max_length=100, null=True, blank=False)
        # path = models.CharField(max_length=150, null=True, blank=False)
        #
        # def __unicode__(self):
        # return self.title