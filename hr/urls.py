from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',

    url(r'^employee/', include('hr.employee.urls')),

    url(r'^department/', include("hr.department.urls")),
)