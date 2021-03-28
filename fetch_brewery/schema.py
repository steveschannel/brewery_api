"""Main GraphQL schema file. Only one for this project."""
import graphene
from .graphql.types.brewery import Brewery as BreweryType
from .graphql.queries.find_breweries import FindBreweries


class Query(graphene.ObjectType):
    help = graphene.String()

    breweries = graphene.List(BreweryType, name=graphene.String(), longitude=graphene.Float(), latitude=graphene.Float(), km=graphene.Int()
                              )

    def resolve_help(self, info, **kwargs):
        return "query { breweries( name: "", longitude: null, latitude: null, km:100 ) { id name city } }"

    def resolve_breweries(self, info, name=None, longitude=None, latitude=None, km=None, *args, **kwargs):

        return FindBreweries(name, longitude, latitude, km)


schema = graphene.Schema(query=Query)
