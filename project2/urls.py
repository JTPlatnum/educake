from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'project2.views.home', name='home'),
<<<<<<< HEAD
    url(r'^start/$', 'project2.views.start', name='start'),
    url(r'^login/$', 'project2.views.login', name='login'),
    url(r'^register/$', 'project2.views.register', name='register'),
=======
    url(r'^start$', 'project2.views.start', name='start'),
>>>>>>> f4a498fb0ad936ded03e14a7ac1047f24d30eb57
    url(r'^search/', include('search.urls', namespace = "search") ),
    url(r'^favorites/', include('favorites.urls', namespace = "favorites") ),
    url(r'^admin/', include(admin.site.urls)),
    
   # url(r'^login/$', 'django.contrib.auth.views.login'),
   # url(r'^logout/$', 'logout_page'),
 
    # Examples:
    # url(r'^$', 'project2.views.home', name='home'),
    # url(r'^project2/', include('project2.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
<<<<<<< HEAD

=======
    url(r'^admin/', include(admin.site.urls)),
>>>>>>> f4a498fb0ad936ded03e14a7ac1047f24d30eb57
)
