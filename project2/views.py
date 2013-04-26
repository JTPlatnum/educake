from django.shortcuts import render
from search import search_helpers

def home(request):  
    data = {"STATES": search_helpers.STATES}
    return render(request, "project2/home.html", data)

def start(request):  
    return render(request, "project2/start.html")