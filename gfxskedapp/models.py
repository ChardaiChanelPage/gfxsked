from __future__ import unicode_literals

from django.db import models

class Requests(models.Model):
	publication_time = models.CharField(max_length=50)
	slug = models.CharField(max_length=10)
	editor = models.CharField(max_length=50)
	reporter = models.CharField(max_length=50)
	graphic_explanation = models.CharField(max_length=500)
	is_data_provided = models.CharField(max_length=3)
	inline_or_standalone = models.CharField(max_length=11)
	graphics_category = models.CharField(max_length=15)

	def __unicode__(self):
		return self.slug + " / " + self.editor + " / " + self.reporter 