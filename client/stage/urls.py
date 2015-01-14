from django.conf.urls import patterns, url
from django.views.generic import ListView
from django.contrib.auth.decorators import permission_required, login_required
from client.models import Stage
from client.stage.views import StageCreateView, StageUpdateView, StageDeleteView

urlpatterns = patterns(
    '',
    url(r'^$', login_required(ListView.as_view(
        model=Stage,
        context_object_name="stages",
        template_name="client/stage/stage.list.html")), name="stage.list"),

    url(r'^add/$',
        permission_required('client.add_stage')(StageCreateView.as_view()), name="stage.add"),

    url(r'^mod/(?P<stage>\d+)/$',
        permission_required('client.change_stage')(StageUpdateView.as_view()), name="stage.edit"),

    url(r'^del/(?P<stage>\d+)/$',
        permission_required('client.delete_stage')(StageDeleteView.as_view()), name="stage.delete"),

)