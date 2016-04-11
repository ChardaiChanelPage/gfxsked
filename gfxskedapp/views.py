from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponse
from gfxskedapp.models import Requests
from django.template import Context, loader
from gfxskedapp.forms import RequestsForm

from .forms import RequestsForm


def index(request):
	requests_list = Requests.objects.all()
	t = loader.get_template('requests/index.html')
	c = Context ({'requests_list': requests_list})
	return render_to_response('requests/index.html', {'requests_list': requests_list}, 
		context_instance=RequestContext(request))


def requests(request):
	t = loader.get_template('requests/request.html')
	return HttpResponse(t.render())


def detailedRequestsView(request):
	print request.method
	if request.method == 'POST': #form has been submitted
		form = RequestsForm(request.POST)
		print 'entered'
		if form.is_valid():
			print 'is valid!'
			requestorName = request.POST.get('requestorName','')
			contactName = request.POST.get('contactName', '')
			contactEmail = request.POST.get('contactEmail', '')
			publishDate = request.POST.get('publishDate', '')
			details = request.POST.get('details', '')
			isExistingArticle = request.POST.get('isExistingArticle', '')
			providedURL = request.POST.get('providedURL','')
			slug = request.POST.get('slug', '')
			r = Requests(requestorName = requestorName, contactName = contactName, contactEmail = contactEmail, details = details, 
			publishDate = publishDate, isExistingArticle = isExistingArticle, providedURL = providedURL, slug = slug, isAssigned = 'no')
			r.save()

	else:
		print 'not valid :('
		form = RequestsForm()

	return render(request, 'requests/detailedRequest.html', { 'form' :form })

	#requests_list = Requests.objects.all()
	#t = loader.get_template('requests/detailedRequest.html')
	#c = Context ({'requests_list': requests_list})
	#return render_to_response('requests/detailedRequest.html', {'requests_list': requests_list}, 
	#	context_instance=RequestContext(request))


def ideaRequestView(request):

	print request.method
	if request.method == 'POST': #form has been submitted
		form = RequestsForm(request.POST)
		print 'entered'
		if form.is_valid():
			print 'is valid!'
			contactName = request.POST.get('contactName', '')
			contactEmail = request.POST.get('contactEmail', '')
			details = request.POST.get('details', '')
			r = Requests(contactName = contactName, contactEmail = contactEmail, details = details)
			r.save()

	else:
		print 'not valid :('
		form = RequestsForm()

	return render(request, 'requests/ideaRequest.html', { 'form' :form })
		
	#requests_list = Requests.objects.all()
	#t = loader.get_template('requests/ideaRequest.html')
	#c = Context ({'requests_list': requests_list})
	#return render_to_response('requests/ideaRequest.html', {'requests_list': requests_list}, 
	#	context_instance=RequestContext(request))
		

def homeView(request):
	requests_list = Requests.objects.all()
	t = loader.get_template('requests/home.html')
	c = Context ({'requests_list': requests_list})
	return render_to_response('requests/home.html', {'requests_list': requests_list}, 
		context_instance=RequestContext(request))


