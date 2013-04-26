from django.http import HttpResponse, HttpResponseRedirect
from search.models import Degree_Level, Degree_Subject, Schools, Programs
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import search
from django.core.validators import validate_email
from django.shortcuts import render
from search import search_helpers

def home(request):
    return render(request, 'project2/home.html')

def start(request):
    return render(request, 'project2/start.html')

def isValidEmail(email):
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False

def login(request):    
    post_email = request.POST['log_email']
    post_pass = request.POST['log_password']
    e_l = []
    if not isValidEmail(post_email):
        e_l.append("Your email address is not valid. Please try again.")    
    if post_email and post_pass:
        u = User.objects.get(email=post_email)
        if u:
            if post_pass == u.password:
#                request.session['log_email'] = u.email
                return HttpResponseRedirect('/search/')
            else:
                e_l.append("Wrong password, try again.")
        else:
            e_l.append("Please enter your email and password")           
    else:
            e_l.append("Please enter your email and password")
    pass_data = {'e_l':e_l}
    return render(request, 'project2/start.html', pass_data)
  
def register(request):
    post_email = request.POST['reg_email']
    post_username = request.POST['reg_username']
    post_password = request.POST['reg_password']
    post_first_name = request.POST['reg_first_name']
    post_last_name = request.POST['reg_last_name']
    e_r = []
    if post_email and post_username and post_password and post_first_name and post_last_name:
        if post_password != request.POST['conf_reg_password']:
            e_r.append("Your passwords do not match. Please try again.")
        if not isValidEmail(post_email):
            e_r.append("Your email address is not valid. Please try again.")
#        if User.objects.get(email=post_email):
#            e_r.append("This email already exists in our system. Please try again.")      
        r = User(email=post_email, username=post_username, password=post_password, is_superuser=0, is_staff=0, first_name=post_first_name, last_name=post_last_name)    
        if r:
            r.save()
            msg = "Thank you for submitting your information, please login above"
            pass_data = {'msg':msg} 
            return render(request,'project2/start.html', pass_data)        
    else:
        e_r.append("Please fill in all fields to register.")
        pass_data = {'e_r':e_r}
        return render(request, 'project2/start.html', pass_data)

def home(request):  
    data = {"STATES": search_helpers.STATES}
    return render(request, "project2/home.html", data)

def start(request):  
    return render(request, "project2/start.html")

