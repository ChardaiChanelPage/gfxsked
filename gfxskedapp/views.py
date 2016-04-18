from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponse
from gfxskedapp.models import Requests
from django.template import Context, loader
from gfxskedapp.forms import RequestsForm
from django.core.mail import send_mail, EmailMessage
from .forms import RequestsForm
from django.contrib import messages


def indexView(request):
	requests_list = Requests.objects.all()
	t = loader.get_template('requests/index.html')
	c = Context ({'requests_list': requests_list})
	return render_to_response('requests/index.html', {'requests_list': requests_list}, 
		context_instance=RequestContext(request))

def detailedRequestsView(request):
	if request.method == 'POST': #form has been submitted
		form = RequestsForm(request.POST)
		if form.is_valid():
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
			messages.success(request, 'Request submitted!')
	else:
		form = RequestsForm()

	return render(request, 'requests/detailedRequest.html', { 'form' :form })


def ideaRequestView(request):
	if request.method == 'POST': #form has been submitted
		form = RequestsForm(request.POST)
		if form.is_valid():
			contactName = request.POST.get('contactName', '')
			contactEmail = request.POST.get('contactEmail', '')
			details = request.POST.get('details', '')
			r = Requests(contactName = contactName, contactEmail = contactEmail, details = details)
			r.save()
			messages.success(request, 'Request submitted!')
	else:
		form = RequestsForm()

	return render(request, 'requests/ideaRequest.html', { 'form' :form })


def homeView(request):
	requests_list = Requests.objects.all()
	t = loader.get_template('requests/home.html')
	c = Context ({'requests_list': requests_list})
	return render_to_response('requests/home.html', {'requests_list': requests_list}, 
		context_instance=RequestContext(request))


