from django.db import models

class Route(models.Model):
	routename = models.CharField(max_length=255)
	icon = models.CharField(max_length=255)
	def __unicode__(self):
		return self.routename

class Cat(models.Model):
	catname = models.CharField(max_length=255)
	colour = models.CharField(max_length=255)
	def __unicode__(self):
		return self.catname

class Point(models.Model):
	route = models.ForeignKey(Route)
	cat = models.ForeignKey(Cat)
	attribution = models.CharField(max_length=255)
	title = models.CharField(max_length=65)
	lat = models.FloatField()
	lon = models.FloatField()
	imageURL = models.URLField(verify_exists=True)
	line2 = models.CharField(max_length=40)
	line3 = models.CharField(max_length=40, blank=True, null=True)
	line4 = models.CharField(max_length=40, blank=True, null=True)
	type_s = models.IntegerField(max_length=11, blank=True, null=True)
	dimension = models.IntegerField(max_length=1, blank=True, null=True)
	alt = models.IntegerField(max_length=10, blank=True, null=True)
	relativeAlt = models.IntegerField(max_length=10, blank=True, null=True)
	actions = models.CharField(max_length=30, blank=True, null=True)
	distance = models.FloatField()
	inFocus = models.IntegerField(max_length=1, default=0)
	doNotIndex = models.IntegerField(max_length=1, default=0)
	showSmallBiW = models.IntegerField(max_length=1, default=1)
	showBiWOnClick = models.IntegerField(max_length=1, default=0)
	pub_date = models.DateTimeField('aanmaakdatum') #aanmaakdatum = date published
	def __unicode__(self):
		return self.title
