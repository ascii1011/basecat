from django.conf.urls import patterns, include, url

urlpatterns = patterns('projects.views',
    url(r'^(?P<pk>\d{1})/$', 'project_dashboard', name='project-dashboard'),
)
