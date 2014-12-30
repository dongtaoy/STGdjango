from django.db import models
from hr.models import Employee
from system.models import Label

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
    visa = models.ForeignKey(Visa, blank=True, null=True)
    expire = models.DateField(blank=True, null=True)

    # Service Information
    STATUS_CHOICES = (
        ("Ongoing", "Ongoing"),
        ("Existing", "Existing"),
        ("Close", "Close")
    )
    status = models.CharField(max_length=10, blank=True, null=True, choices=STATUS_CHOICES,
                              default="Ongoing")  ## ChoiceField todo
    referal = models.ForeignKey(Employee, blank=True, null=True, related_name="ref")  # todo
    consultant = models.ForeignKey(Employee, blank=True, null=True, related_name="con")  # todo
    clientManager = models.ForeignKey(Employee, blank=True, null=True, related_name="cm")  # todo
    # stage = models.ManyToManyField(Stage) ## todo
    serviceFee = models.FloatField(blank=True, null=True)
    thirdPartyFeeReceived = models.FloatField(blank=True, null=True)
    thirdPartyFeePaid = models.FloatField(blank=True, null=True)

    # Others
    note = models.TextField(blank=True, null=True)


class Institution(models.Model):
    name = models.CharField(max_length=100)
    label = models.ForeignKey(Label, null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return str(self.name)

#
# class Coe(models.Model):
#     client = models.ForeignKey(Client)
#     institution = models.ForeignKey(Institution)
#     start = models.DateField()
#     end = models.DateField()
#
#     totalTuitionFee = models.FloatField(blank=True, null=True)
#     totalReceivedFee = models.FloatField(blank=True, null=True)
#     totalPaymentFee = models.FloatField(blank=True, null=True)
#     totalCommissionClaimed = models.FloatField(blank=True, null=True)
#     totalCommissionRecevied = models.FloatField(blank=True, null=True)
#     bonus = models.FloatField(blank=True, null=True)
#     referalCommission = models.FloatField(blank=True, null=True)
#     consultantCommission = models.FloatField(blank=True, null=True)
#
#     description = models.TextField(blank=True, null=True)

#
#
#
# class Payment(models.Model):
#     coe = models.ForeignKey(Coe)
#
#     receivedAmount = models.FloatField(blank=True, null=True)
#     receivedDate = models.DateField(blank=True, null=True)
#     paidAmount = models.FloatField(blank=True, null=True)
#     paidDate = models.DateField(blank=True, null=True)
#     commssionClaimed = models.FloatField(blank=True, null=True)
#     commssionRecevied = models.FloatField(blank=True, null=True)
#
#     nextDueDate = models.DateField(blank=True, null=True)
