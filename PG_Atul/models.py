from django.db import models

from django.contrib import admin

class Photos(models.Model):
	capt = models.CharField(max_length=30)
	desc = models.CharField(max_length=100)
	img = models.ImageField(null=True, blank=True)





admin.site.register(Photos)