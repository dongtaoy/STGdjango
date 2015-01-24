from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'STGdjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'django.contrib.auth.views.password_change',
        {'template_name': 'system/password/password.change.html',
         'post_change_redirect': '/'}, name="password.reset"),
)
