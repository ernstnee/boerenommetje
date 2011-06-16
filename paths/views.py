# Create your views here.

from django.contrib.gis.geos import Point
from paths.models import PointOfInterest
from layar import LayarView, POI
import json, datetime

class BoerenommetjeLayar(LayarView):

    # make sure to accept **kwargs
    def get_boerenommetje_queryset(self, latitude, longitude, radius, **kwargs):
        return PointOfInterest.objects.filter(location__distance_lt=(Point(longitude, latitude), radius))

    def poi_from_boerenommetje_item(self, item):
        return POI(id=item.id, lat=item.location.y, lon=item.location.x, title=item.name,
                    line2=item.route_name, line3='Distance: %distance%')

# create an instance of BoerenommetjeLayar
boerenommetje_layar = BoerenommetjeLayar()



import json
import datetime
from django.http import HttpResponse
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from paths.models import *

def get_pt_or_bbox(rg):
    """
    parse out lat/lon and return geos geom
    """
    lat = rg.get('lat','')
    lon = rg.get('lon','')
    if lat and lon: 
        return Point(float(lon), float(lat), srid=4326)
    return False


def render_to_layar(results, ltype):
    hotspots = []
    for t in results:
        #todo, generalize dict mapping for different layers
        if ltype == 'boerenommetje':
             if t.attribution == 'LARCENY/THEFT': type=1
             elif t.attribution == 'ASSAULT': type=2
             else: type=0
             title =  t.title
             line2 = t.line2
             line3 = t.line3
             
        if ltype == 'boerenommetje':
             type = 1
             title = t.title
             line2 = t.line2
             line3 = ''
             
        d = {'actions': [],
             'attribution': 'datasf.org',
             'distance': t.distance.m,
             'id': str(t.pk),
             'imageURL': imageURL,
             'lat': int(t.lat * 1000000),
             'line2': line2,
             'line3': line3,
             'line4': '',
             'lon': int(t.lon * 1000000),
             'title': title,
             'type': type}
        hotspots.append(d)
         
    response = HttpResponse()
    j = json.dumps({'hotspots':hotspots,
        "layer": ltype,
        "errorString": "ok", 
        "morePages": False,  #todo, add paging
        "errorCode": 0, 
        "nextPageKey": None})
    
    response.write(j)
    response['Content-length'] = str(len(response.content))
    response['Content-Type'] = 'application/json'
    return response

def layar_base(request):
    #these are the params layar passes us that we care about, for now
    geom = get_pt_or_bbox(request.GET)
    date_filter = request.GET.get('CUSTOM_SLIDER','')
    category = request.GET.get('RADIOLIST','')
    layer_name = request.GET.get('layerName','') 
    distance = int(request.GET.get('RADIUS', 1500))

    if layer_name == 'boerenommetje':
        res = PointOfInterest.objects.all()
        if date_filter:
            df = int(float(date_filter))
            then = datetime.datetime.now() - datetime.timedelta(days=df)
            dt = '%.2d/%.2d/%s' % (then.month, then.day, then.year)
            res = res.filter(date__gte=dt)

        if category and not category == 'any':
            res = res.filter(category=category)

    elif layer_name == 'bluezones':
        res = Bluezone.objects.all()
    
    res = res.filter(
        geom_4326__distance_lte=(
            geom, D(m=distance))
            ).distance(geom).order_by('distance')
            
    return render_to_layar(res[:25], layer_name) #todo, add paging
