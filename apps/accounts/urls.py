from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^nav/', 'accounts.views.nav', name='nav'), 

    # login URLs:
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', 
        {'next_page': '/'}, 
        name='logout'),

    url(r'^register/', 'accounts.views.register', name='register'), 
)