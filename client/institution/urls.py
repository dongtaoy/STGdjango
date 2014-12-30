from django.conf.urls import patterns, url
from django.views.generic import ListView
from django.contrib.auth.decorators import permission_required, login_required
from client.institution.views import InstitutionCreateView, InstitutionUpdateView, InstitutionDeleteView
from client.models import Institution

urlpatterns = patterns(
    '',
    url("^$", login_required(ListView.as_view(
        model=Institution,
        template_name="client/institution/institution.list.html",
        context_object_name="institutions"
    )), name="institution.list"),
    url("^add/$",
        permission_required("client.add_institution")(InstitutionCreateView.as_view()), name="institution.add"),
    url("^mod/(?P<institution>\d+)/$",
        permission_required("client.change_institution")(InstitutionUpdateView.as_view()), name="institution.change"),
    url("^del/(?P<institution>\d+)/$",
        permission_required("client.delete_institution")(InstitutionDeleteView.as_view()), name="institution.delete"),
)