from django.db import models
from hr.models import Employee


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


class Client(models.Model):
    # Personal Information
    name = models.CharField(max_length=100)
    preferredName = models.CharField(max_length=100, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=100, blank=True, null=True)  ## ChoiceField???? todo
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    onshore = models.BooleanField(default=True)

    # Visa Information
    visa = models.ForeignKey(Visa)
    expire = models.DateField(blank=True, null=True)

    # Service Information
    status = models.CharField(max_length=100)  ## ChoiceField todo
    referal = models.ForeignKey(Employee, blank=True, null=True, related_name="ref")  # todo
    consultant = models.ForeignKey(Employee, blank=True, null=True, related_name="con")  # todo
    clientManager = models.ForeignKey(Employee, blank=True, null=True, related_name="c")  # todo
    # stage = models.ManyToManyField(Stage) ## todo
    serviceFee = models.FloatField(blank=True, null=True)
    thirdPartyFeeReceived = models.FloatField(blank=True, null=True)
    thirdPartyFeePaid = models.FloatField(blank=True, null=True)

    # Others
    note = models.TextField(blank=True, null=True)

