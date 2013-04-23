from django.http import HttpResponse, HttpResponseRedirect
from search.models import Degree_Level, Degree_Subject, Schools, Programs
from django.shortcuts import render, get_object_or_404


def home(request):
<<<<<<< HEAD
    return render(request, 'project2/home.html')

def login(request):
    return render(request, 'project2/login.html')

=======
    return render(request, "project2/welcome.html")
>>>>>>> 4424a47e79f048a4a94e838c49f1c29b3e4f9d9d
