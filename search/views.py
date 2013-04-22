from django.http import HttpResponse, HttpResponseRedirect
from search.models import Degree_Level, Degree_Subject, Schools, Programs
from django.shortcuts import render, get_object_or_404
# from django.core.urlresolvers import reverse


def new(request):
    return HttpResponse("Base search page (guests) <br> <a href=''></a>")

def results(request):
    return HttpResponse("Results page <br> <a href=''></a>")

#index
#new
#create
#show
#edit
#update
#destroy