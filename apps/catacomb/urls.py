from django.conf.urls import patterns, include, url

from .views import BrainView

urlpatterns = patterns('catacombs.views',
    url(r'^$', 'main', name='main'),
    url(r'^brain/', BrainView.as_view(), name='brain'),
)