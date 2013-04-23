# Create your views here.

from django.http import HttpResponse
from django.template import Context, loader
from favorites.models import Favorites


def index(request):
    latest_favorites_list = Favorites.objects.order_by('created_at')[:5]
    template = loader.get_template('favorites/index.html')
    context = Context({
        'latest_favorites_list' : latest_favorites_list,
        })
  #  output = ', '.join([str(p.user_id) for p in latest_favorites_list])
    return HttpResponse(template.render(context))

def detail(request, favorites_id):
    return HttpResponse("You're looking at favorites %s." % favorites_id)

def results(request, favorites_id):
    return HttpResponse("You're looking at the results of favorites %s." % favorites_id)

def vote(request, favorites_id):
    return HttpResponse("You're voting on favorites %s." % favorites_id)
