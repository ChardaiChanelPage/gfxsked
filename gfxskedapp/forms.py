from django import forms

class RequestsForm(forms.Form):
	
	requestorName = forms.CharField(max_length=50, required=False)
	contactName = forms.CharField(max_length=50, required=True)
	contactEmail = forms.EmailField(required=True)
	publishDate = forms.CharField(max_length=50, required=False)
	details = forms.CharField(max_length=500, required=True)
	isExistingArticle = forms.CharField(max_length=3, required=False)
	providedURL = forms.CharField(max_length=50, required=False)
	slug = forms.CharField(max_length=10, required=False)
	isAssigned = forms.CharField(max_length=3, required=False)
