from django.conf.urls import patterns, include, url

from accounts import urls as _accounts
from projects import urls as _projects

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'basecat.views.home', name='home'),
    #url(r'^brain/', BrainView.as_view(), name='brain'),

    url(r'^account/', include(_accounts)),
    url(r'^voynich/', include(_projects)),

    url(r'^admin/', include(admin.site.urls), name='admin'),
)
