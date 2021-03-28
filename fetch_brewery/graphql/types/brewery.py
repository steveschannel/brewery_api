
from breweries.models import Brewery as BreweryModel
from graphene_django import DjangoObjectType
import graphene


class Brewery(DjangoObjectType):
    name = graphene.String()
    latitude = graphene.Float()
    longitude = graphene.Float()

    class Meta:
        model = BreweryModel
        exclude_fields = ['point']

    def resolve_name(self, info, **kwargs):
        return self.name

    def resolve_brewery_type(self, info, **kwargs):
        return self.brewery_type

    def resolve_county_province(self, info, **kwargs):
        return self.county_province

    def resolve_postal_code(self, info, **kwargs):
        return self.postal_code

    def resolve_website_url(self, info, **kwargs):
        return self.website_url

    def resolve_phone(self, info, **kwargs):
        return self.phone

    def resolve_latitude(self, info, **kwargs):
        return self.latitude

    def resolve_longitude(self, info, **kwargs):
        return self.longitude

    def resolve_city(self, info, **kwargs):
        return self.city

    def resolve_state(self, info, **kwargs):
        return self.state
