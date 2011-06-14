from paths.models import PointOfInterest, Action
from django.contrib import admin
import settings

class PointOfInterestAdmin(admin.ModelAdmin):
	fieldsets = (
		(None, { 
				'fields': ('attribution', 'category', 'title', 'imageURL', 'location', 'line2', 'line3', 'line4', 'pub_date', 'lat', 'lon')
		}),
	)
	list_filter = ('attribution',)
	list_display = ('__unicode__', 'attribution')
	search_fields = ['title']
	
	class Media:
		js = [
            'http://code.jquery.com/jquery-1.4.2.min.js', 
            'http://maps.google.com/maps/api/js?sensor=false', 
            settings.MEDIA_URL +'/admin/long-lat-render.js'
        ]

admin.site.register(PointOfInterest, PointOfInterestAdmin)
admin.site.register(Action)

