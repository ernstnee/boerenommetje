from paths.models import PointOfInterest, Action, TypeOfAction, Route
from django.contrib import admin
import settings

class PointOfInterestAdmin(admin.ModelAdmin):
	fieldsets = (
		(None, { 
				'fields': ('attribution', 'category', 'title', 'imageURL', 'line2', 'line3', 'line4', 'pub_date', 'lat', 'lon')
		}),
	)
	#list_filter = ('attribution',)
	list_display = ('__unicode__', 'attribution', 'category')
	search_fields = ['title']
	
	class Media:
		js = [
            'http://code.jquery.com/jquery-1.4.2.min.js', 
            'http://maps.google.com/maps/api/js?sensor=false', 
            settings.MEDIA_URL +'/admin/long-lat-render.js'
        ]

class ActionAdmin(admin.ModelAdmin):
	fieldsets = (
		(None, { 
				'fields': ('pointofi', 'typeofaction', 'url')
		}),
	)

admin.site.register(PointOfInterest, PointOfInterestAdmin)
admin.site.register(Action, ActionAdmin)
admin.site.register(Route)
admin.site.register(TypeOfAction)
