from django.db import models

# Create your models here.
class Keywords(models.Model):
	keyword = models.CharField(max_length= 50, blank=False)
	search_date = models.DateTimeField(auto_now_add=True)
	count = models.IntegerField(default=0)
	page = models.CharField(max_length=50, blank=False)


class MitbbsPages(models.Model):
	cn_page = models.CharField(max_length=50, blank=False)
	en_page = models.CharField(max_length=50, blank=False)