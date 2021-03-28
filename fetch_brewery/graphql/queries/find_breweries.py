import graphene

from breweries.models import Brewery
from django.db.models import Q
from ..types.brewery import Brewery as BreweryType
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance


def FindBreweries(name, longitude, latitude, km):

    if name and latitude and longitude:
        search_pnt = Point(longitude, latitude, srid=4326)
        qs = Brewery.objects.filter(
            name__icontains=name, point__dwithin=(search_pnt, Distance(km=km)))

    elif name and not latitude:
        qs = Brewery.objects.filter(name__icontains=name)

    elif not name and latitude and longitude:
        search_pnt = Point(longitude, latitude, srid=4326)
        qs = Brewery.objects.filter(
            point__dwithin=(search_pnt, Distance(km=km)))

    else:
        qs = Brewery.objects.all()

    return qs
