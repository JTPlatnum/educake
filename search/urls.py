from django.conf.urls import patterns, include, url
from search import views

urlpatterns = patterns('',                
    url(r'^$', views.index, name='search'),
<<<<<<< HEAD
=======
    url(r'^filter$', views.filter, name='filter'),
>>>>>>> f4a498fb0ad936ded03e14a7ac1047f24d30eb57
    )