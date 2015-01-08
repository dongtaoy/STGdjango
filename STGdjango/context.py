

__author__ = 'dongtaoy'


def common(request):
    from system.models import Sidebar
    from client.models import Payment
    import datetime

    now = datetime.datetime.now()
    max_date = now.date() + datetime.timedelta(30)

    return {"path": request.path,
            "Sidebars": Sidebar.objects.filter(parent=None),
            "Payments": Payment.objects.filter(nextDueDate__range=[now, max_date]),
            "Now": now,
    }