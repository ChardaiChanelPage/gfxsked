from django.shortcuts import render
from django.http import HttpResponse
from gfxskedapp.models import Requests
from django.template import Context, loader

# Create your views here.
def index(request):
	requests_list = Requests.objects.all()
	t = loader.get_template('requests/index.html')
	c = Context ({'requests_list': requests_list})
	return HttpResponse(t.render(c))

def requests(request):
	t = loader.get_template('requests/request.html')
	return HttpResponse(t.render())
	#return HttpResponse("You are viewing the request page")