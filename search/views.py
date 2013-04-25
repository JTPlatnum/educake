from django.http import HttpResponse, HttpResponseRedirect
from search.models import Degree_Level, Degree_Subject, Schools, Programs
from django.shortcuts import render, get_object_or_404
# from django.core.urlresolvers import reverse

def index(request):
    degree_levels = Degree_Level.objects.all()
    degree_subjects = Degree_Subject.objects.all()
    schools_all = Schools.objects.all()
    schools = []
    for school in schools_all:
        schools.append(school.name)
        
    programs_all = Programs.objects.all()
    programs = []
    for program in programs_all:
        school = Schools.objects.get(id = program.school_id)
        data = {}
        data["p_name"] = program.name
        data["p_description"] = program.description
        data["s_name"] = school.name
        data["s_city"] = school.city
        data["s_state"] = school.state
        programs.append(data)
    
    pass_data = {
        "degree_levels": degree_levels,
        "degree_subjects": degree_subjects,
        "schools": schools,
        "programs": programs
    }
    
    return render(request, "search/search.html", pass_data)
