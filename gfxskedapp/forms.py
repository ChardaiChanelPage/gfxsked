from django import forms
from django.contrib.admin import widgets
from django.forms.extras.widgets import SelectDateWidget
from django.forms import ModelForm, Form
import datetime

class RequestsForm(forms.Form):

	requestorName = forms.CharField(max_length=50, required=False)
	contactName = forms.CharField(max_length=50, required=True)
	contactEmail = forms.EmailField(required=True)
	#publishDate = forms.DateField(widget=SelectDateWidget, required=False)
	publishDate = forms.CharField(max_length=50, required=False)
	details = forms.CharField(max_length=500, required=True)
	isExistingArticle = forms.CharField(max_length=3, required=False)
	providedURL = forms.CharField(max_length=50, required=False)
	slug = forms.CharField(max_length=10, required=False)
	isAssigned = forms.CharField(max_length=3, required=False)
	status = forms.CharField(max_length=20, required=False)
