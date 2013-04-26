from django.conf.urls import patterns, include, url
from search import views

urlpatterns = patterns('',                
    url(r'^$', views.index, name='search'),
    url(r'^filter$', views.filter, name='filter'),
    )