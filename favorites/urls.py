from django.conf.urls import patterns, url

from favorites import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    # ex: /favorites/3/
    url(r'^(?P<favorites_id>\d+)/$', views.detail, name='detail'),
    # ex: /favorites/3/results/
    url(r'^(?P<favorites_id>\d+)/results/$', views.results, name='results'),
    # ex: /favorites/5/vote/
    url(r'^(?P<favorites_id>\d+)/vote/$', views.vote, name='vote'),    
)