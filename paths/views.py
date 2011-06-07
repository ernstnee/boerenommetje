# Create your views here.

from django.contrib.gis.geos import Point
from paths.models import PointOfInterest
from layar import LayarView, POI

class BoerenommetjeLayar(LayarView):

    # make sure to accept **kwargs
    def get_boerenommetje_queryset(self, latitude, longitude, radius, **kwargs):
        return PointOfInterest.objects.filter(distance=(Point(longitude, latitude), radius))

    def poi_from_boerenommetje_item(self, item):
        return POI(id=item.id, lat=item.location.y, lon=item.location.x, title=item.name,
                    line2=item.route_name, line3='Distance: %distance%')

# create an instance of BoerenommetjeLayar
boerenommetje_layar = BoerenommetjeLayar()
