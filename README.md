# brewery_api
Assessment for fetch. Filters breweries in georgia by name and location.

This api will run at localhost 8000, and you will be able to query the API using graphQL's UI at http://localhost:8000/graphql.

#Interacting with the API

![image](https://user-images.githubusercontent.com/31490008/112763752-c91e2700-8fd3-11eb-98f5-50c49b2444c7.png)

Queries are in the following format, and you can request any field (with the exception of the point field, for the model).

Ex. 1 (Query without passing search params e.g get all breweries in dataset + all fields)

"""

query {
	breweries {
    id
	  name
    breweryType
    websiteUrl
    phone
    city
    state
    country
    updatedAt
    createdAt
    postalCode
	}
}

"""

Ex. 2 (Query without passing name param e.g get all breweries within passed 100-km range of point unput while only requesting the id, name and city )

"""

query {
	breweries(name: "", longitude: -84.435719, latitude: 33.792460, km:100) {
    id
	  name
    city
	}
}

"""

##Stack 

This uses docker for setup. 

Django (Geodjango) + Graphene (GraphQL) + Postgres (GIS extensions) + Docker.

## Setup

Start by building the container so all the dependencies are installed:

docker-compose build

Start the container:

docker-compose up -d

Apply migrations and Load fixtures:

docker-compose run --rm api ./manage.py migrate

In the event that the connection isnt active upon running the last step, restart the service:

docker-compose restart api



The API should now be running, check the guide above to querying the DB.

You can shut down the container:

docker-compose down


Load additional fixtures:

docker-compose run --rm api ./manage.py loaddata --app breweries fetch_brewery/fixtures/["fixture name"]

Make migrations:

docker-compose run --rm api ./manage.py makemigrations





