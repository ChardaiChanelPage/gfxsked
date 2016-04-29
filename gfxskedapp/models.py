from __future__ import unicode_literals

from django.db import models

class Requests(models.Model):

	requestorName = models.CharField(max_length=50)
	contactName = models.CharField(max_length=50)
	contactEmail = models.EmailField()
	publishDate = models.CharField(max_length=50)
	details = models.CharField(max_length=500)
	isExistingArticle = models.CharField(max_length=3)
	providedURL = models.CharField(max_length=50)
	slug = models.CharField(max_length=10)
	isAssigned = models.CharField(max_length=3)
	status = models.CharField(max_length=20)
	

	def __unicode__(self):
		return self.slug + " / " + self.publishDate + " / " + self.contactName