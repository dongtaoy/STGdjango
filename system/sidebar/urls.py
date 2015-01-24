__author__ = 'dongtaoy'
from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required, permission_required
from system.sidebar.views import SidebarListView, SidebarCreateView, SidebarDeleteView, SidebarUpdateView

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'STGdjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', login_required(SidebarListView.as_view()), name='sidebar.list'),

    url(r'^add/$',
        permission_required('system.add_sidebar')(SidebarCreateView.as_view()), name='sidebar.add'),

    url(r'^mod/(?P<sidebar>\d+)/$',
        permission_required('system.change_sidebar')(SidebarUpdateView.as_view()), name='sidebar.mod'),

    url(r'^del/(?P<sidebar>\d+)/$',
        permission_required('system.change_sidebar')(SidebarDeleteView.as_view()), name='sidebar.delete'),
)
