from django.db import models

class Point(models.Model):
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

class Action(models.Model):
	METHOD_CHOICES = (
        ('GET', 'GET'),
        ('POST', 'POST'),
	)
	point = models.ForeignKey(Point)		
	label = models.CharField(max_length=255)
	url = models.CharField(max_length=255)
	autoTriggerRange = models.IntegerField(max_length=10, blank=True, null=True)
	autoTriggerOnly = models.IntegerField(max_length=1, blank=True, null=True)
	contentType = models.CharField(max_length=255, default='application/vnd.layar.internal')
	method = models.CharField(max_length=4, default='GET', choices=METHOD_CHOICES)
	activityType = models.IntegerField(max_length=2)
	params = models.CharField(max_length=255, null=True)
	closeBiw = models.IntegerField(max_length=1, default=0)
	showActivity = models.IntegerField(max_length=1, default=1)
	activityMessage = models.CharField(max_length=255, null=True)
	def __unicode__(self):
		return self.label
