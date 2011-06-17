from django.contrib.gis.db import models
from paths.widgets import *

class PointOfInterest(models.Model):
	CATEGORY_CHOICES = (
		('Weetjes', 'Weetjes'),
		('Aanbiedingen', 'Aanbiedingen'),
		('Vermaak', 'Vermaak'),
	)
	attribution = models.CharField('Route', max_length=65, help_text="Use puns liberally")
	title = models.CharField('Titel', max_length=65)
	lat = models.FloatField()
	lon = models.FloatField()
	category = models.CharField('Categorie', max_length=40, default='Weetjes', choices=CATEGORY_CHOICES)
	imageURL = models.ImageField('Afbeelding', upload_to='/media/img')
	line2 = models.CharField('Regel 2', max_length=40)
	line3 = models.CharField('Regel 3', max_length=40, blank=True, null=True)
	line4 = models.CharField('Regel 4', max_length=40, blank=True, null=True)
	type_s = models.IntegerField('Type Layer', max_length=11, blank=True, null=True)
	dimension = models.IntegerField(max_length=1, blank=True, null=True)
	alt = models.IntegerField(max_length=10, blank=True, null=True)
	relativeAlt = models.IntegerField(max_length=10, blank=True, null=True)
	actions = models.CharField(max_length=30, blank=True, null=True)
	inFocus = models.IntegerField(max_length=1, default=0)
	doNotIndex = models.IntegerField(max_length=1, default=0)
	showSmallBiW = models.IntegerField(max_length=1, default=1)
	showBiWOnClick = models.IntegerField(max_length=1, default=0)
	pub_date = models.DateTimeField('aanmaakdatum') #aanmaakdatum = date published
	def __unicode__(self):
		return self.title

class Action(models.Model):
	ACT_CHOICES = (
        (1, 'Website'),
        (2, 'Audio') ,
        (3, 'Video'),
        (4, 'Bellen'),
        (5, 'E-mail'),
	)
	pointofi = models.ForeignKey(PointOfInterest, verbose_name="POI")		
	label = models.CharField(max_length=10, help_text='Bijv. vind ons op..')
	url = models.CharField('URL', max_length=255)
	autoTriggerRange = models.IntegerField(max_length=10, blank=True, null=True)
	autoTriggerOnly = models.IntegerField(max_length=1, blank=True, null=True)
	contentType = models.CharField(max_length=255, default='INFO'[0])
	method = models.CharField(max_length=4, default='GET')
	activityType = models.IntegerField(max_length=2, default='INFO'[0], choices=ACT_CHOICES	)
	params = models.CharField(max_length=255, blank=True, null=True)
	closeBiw = models.IntegerField(max_length=1, default=0)
	showActivity = models.IntegerField(max_length=1, default=1)
	activityMessage = models.CharField(max_length=255, null=True)
	def __unicode__(self):
		return self.label

