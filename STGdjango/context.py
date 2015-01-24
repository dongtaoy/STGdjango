from django.contrib.auth.models import Group

__author__ = 'dongtaoy'


def common(request):
    from system.models import Sidebar
    from client.models import Payment
    from hr.models import Employee
    import datetime

    now = datetime.datetime.now()
    max_date = now.date() + datetime.timedelta(30)

    payments = Payment.objects.filter(nextDueDate__range=[now, max_date])
    count = 0

    for payment in payments:
        if not payment.nextPayment.count():
            count += 1

    return {"path": request.path,
            "Sidebars": Sidebar.objects.filter(parent=None),
            "Payments": Payment.objects.filter(nextDueDate__range=[now, max_date]),
            "PaymentCount": count,
            "Now": now,
            "User": request.user,
            "UserGroup": request.user.groups.all(),
            "Consultant": Group.objects.filter(name="Consultant"),
            "Accountant": Group.objects.exclude(name="Consultant"),
            "Manager": Group.objects.filter(name="Manager")
    }
