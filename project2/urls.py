from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'project2.views.home', name='home'),
    url(r'^start/$', 'project2.views.start', name='start'),
    url(r'^login/$', 'project2.views.login', name='login'),
    url(r'^register/$', 'project2.views.register', name='register'),
    url(r'^search/', include('search.urls', namespace = "search") ),
    url(r'^favorites/', include('favorites.urls', namespace = "favorites") ),
    url(r'^admin/', include(admin.site.urls)),
)    
