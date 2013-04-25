from django.http import HttpResponse, HttpResponseRedirect
from search.models import Degree_Level, Degree_Subject, Schools, Programs
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import search
from django.core.validators import validate_email

def home(request):
    return render(request, 'project2/home.html')

def start(request):
    return render(request, 'project2/start.html')

def login(request):    
    post_email = request.POST['log_email']
    post_pass = request.POST['log_password']
    e = []
    if not isValidEmail(post_email):
        e.append("Your email address is not valid. Please try again.")    
    if post_email and post_pass:
        u = User.objects.get(email=post_email)
        if u:
            if post_pass == u.password:
#                request.session['log_email'] = u.email
                return HttpResponseRedirect('/search/')
            else:
                e.append("Wrong password, try again.")
        else:
            e.append("Please enter your email and password")           
    else:
            e.append("Please enter your email and password")
    pass_data = {'e':e}
    return HttpResponseRedirect('/start/', pass_data)
        
def isValidEmail(email):
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False
    
def register(request):
    post_email = request.POST['reg_email']
    post_username = request.POST['reg_username']
    post_password = request.POST['reg_password']
    post_first_name = request.POST['reg_first_name']
    post_last_name = request.POST['reg_last_name']
    if post_email and post_username and post_password and post_first_name and post_last_name:
        if post_password != request.POST['conf_reg_password']:
            return HttpResponse("Your passwords do not match. Please try again.")
        if not isValidEmail(post_email):
            return HttpResponse("Your email address is not valid. Please try again.")
#        if User.objects.get(email=post_email):
#            return HttpResponse("This email already exists in our system. Please try again.")      
        r = User(email=post_email, username=post_username, password=post_password, is_superuser=0, is_staff=0, first_name=post_first_name, last_name=post_last_name)    
        if r:
            r.save()
            msg = "Thank you for submitting your information, please login above"
            pass_data = {'msg':msg} 
            return render(request,'project2/start.html', pass_data)        
    else:
        return HttpResponse("Please fill in all fields to register.")
