from django.http import HttpResponse, HttpResponseRedirect
from search.models import Degree_Level, Degree_Subject, Schools, Programs
from django.shortcuts import render, get_object_or_404
# from django.core.urlresolvers import reverse

def guest(request):
    return render(request, "search/guest.html")

def user(request):
    return render(request, "search/user.html")

#index
#new
#create
#show
#edit
#update
#destroy