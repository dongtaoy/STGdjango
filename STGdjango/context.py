__author__ = 'dongtaoy'


def common(request):
    from system.models import Sidebar

    return {"path": request.path,
            "Sidebars": Sidebar.objects.filter(parent=None)}