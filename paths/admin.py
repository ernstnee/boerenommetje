from paths.models import PointOfInterest, Action
from django.contrib import admin
import settings

class ActionInline(admin.StackedInline):
	model = Action
	extra = 4	
	fieldsets = (
		(None, { 
				'fields': ('pointofi', 'label', 'activityType', 'url')
		}),
	)

class PointOfInterestAdmin(admin.ModelAdmin):
	fieldsets = (
		(None, { 
				'fields': ('attribution', 'category', 'title', 'imageURL', 'line2', 'line3', 'line4', 'pub_date', 'lat', 'lon')
		}),
	)
	list_filter = ('attribution', 'category')
	list_display = ('__unicode__', 'attribution', 'category')
	search_fields = ['title']
	inlines = [ActionInline]

	class Media:
		js = [
            'http://code.jquery.com/jquery-1.4.2.min.js', 
            'http://maps.google.com/maps/api/js?sensor=false', 
            settings.MEDIA_URL +'/admin/long-lat-render.js'
        ]

admin.site.register(PointOfInterest, PointOfInterestAdmin)
