# brewery_api
Assessment for fetch. Filters breweries in georgia by name and location.

##Stack 

This uses docker for setup. 

Django (Geodjango) + Graphene (GraphQL) + Postgres (GIS extensions) + Docker.

## Setup

docker-compose build

docker-compose run --rm api ./manage.py loaddata --app breweries fetch_brewery/fixtures/breweries.json

docker-compose run --rm api ./manage.py migrate

docker-compose run --rm api ./manage.py makemigrations

docker-compose up -d 

docker-compose down
