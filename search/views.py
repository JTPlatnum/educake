from django.http import HttpResponse, HttpResponseRedirect
from search.models import Degree_Level, Degree_Subject, Schools, Programs
from django.shortcuts import render, get_object_or_404
import search_helpers

# from django.core.urlresolvers import reverse

def index(request):
    post_program = request.POST.get('program')
    post_state = request.POST.get('states')
    post_city = request.POST.get('city')
    
    degree_levels = Degree_Level.objects.all()
    degree_subjects = Degree_Subject.objects.all()
    schools = Schools.objects.all()
    
    # get all programs matching search keywords
    program_matches = []
    program_keywords = search_helpers.get_keywords(post_program)
    for keyword in program_keywords:
        query_results = Programs.objects.filter(name__icontains = keyword )
        if query_results:
            for result in query_results:
                if result not in program_matches:
                    program_matches.append(result) 
    
    # if a state was chosen, filter for that state
    if post_state:
        if post_state.lower() != "state":
            for program in program_matches:
                if program.school.state.lower() != post_state.lower():
                    program_matches.remove(program)
    
    # if a city was chosen, filter for that city            
    if post_city:
        for program in program_matches:
            if program.school.city.lower() != post_city.lower():
                program_matches.remove(program)        
                    
    programs = []        
    for program in program_matches:
        school = Schools.objects.get(id = program.school_id)
        data = {}
        data["p_name"] = program.name
        data["p_description"] = program.description
        data["s_name"] = school.name
        data["s_city"] = school.city
        data["s_state"] = school.state
        programs.append(data)
    
    pass_data = {
        "STATES": search_helpers.STATES,
        "degree_levels": degree_levels,
        "degree_subjects": degree_subjects,
        "schools": schools,
        "programs": programs
    }
    
    request.session['current_results'] = programs
    
    return render(request, "search/search.html", pass_data)

def filter(request):
    degree_levels = Degree_Level.objects.all()
    degree_subjects = Degree_Subject.objects.all()
    schools = Schools.objects.all()
    
    current_results = request.session['current_results']
    
#    if 'levels' in request.POST['levels']:
    level_filter = request.POST.getlist('levels')
    school_filter = request.POST.getlist('schools')
    subject_filter = request.POST.getlist('subjects')
    
    if level_filter:
        match = False
        for result in current_results:
            level = Programs.objects.get(name=result['p_name']).degree_level.name
            if level in level_filter:
                match = True
        if not match:
            request.session['current_results'].remove(result)
                
    if school_filter:
        match = False
        for result in current_results:
            if result['s_name'].lower() in map(unicode.lower, school_filter): #school_filter.lower():
                match = True
        if not match:
            request.session['current_results'].remove(result)
                
    if subject_filter:
        match = False
        for result in current_results:
            subject = Programs.objects.get(name=result['p_name']).degree_subject.name
            if subject in subject_filter:
                match = True
        if not match:
            request.session['current_results'].remove(result)
    
    programs = request.session['current_results']
    
    pass_data = {
        "STATES": search_helpers.STATES,
        "degree_levels": degree_levels,
        "degree_subjects": degree_subjects,
        "schools": schools,
        "programs": programs
    }        
    
    return render(request, "search/search.html", pass_data)

