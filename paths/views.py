# Create your views here.

from django.contrib.gis.geos import Point
from paths.models import Point
from layar import LayarView, POI

class PointLayar(LayarView):

    # make sure to accept **kwargs
    def get_point_queryset(self, latitude, longitude, radius, **kwargs):
        return Point.objects.filter(location__distance_lt=(Point(longitude, latitude), radius))

    def poi_from_paths_item(self, item):
        return POI(id=item.id, lat=item.location.y, lon=item.location.x, title=item.name,
                    line2=item.route_name, line3='Distance: %distance%')

# create an instance of PointLayar
paths_layar = PointLayar()
