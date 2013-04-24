from django.http import HttpResponse, HttpResponseRedirect
from search.models import Degree_Level, Degree_Subject, Schools, Programs
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import search

def home(request):
    return render(request, 'project2/home.html')

def start(request):
    return render(request, 'project2/start.html')

def login(request):    
    post_email = request.POST['log_email']
    post_pass = request.POST['log_password']
    if post_email and post_pass:
        u = User.objects.get(email=post_email)
        if u:
            if post_pass == u.password:
                return HttpResponseRedirect('/search/')
            else:
                return HttpResponse("Wrong password, try again")
        else:
            return HttpResponse("Please enter your email and password")           
    else:
            return HttpResponse("Please enter your email and password")
        
def register(request):
#    post_email = request.POST['reg_email']
#    post_username = request.POST['reg_username']
#    post_password = request.POST['reg_password']
#    post_first_name = request.POST['reg_first_name']
#    post_last_name = request.POST['reg_last_name']
    return HttpResponse(request.POST)

