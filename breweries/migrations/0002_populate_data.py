# Generated by Django 3.1.7 on 2021-03-28 13:49

import django.contrib.gis.db.models.fields
from django.db import migrations
from django.contrib.gis.geos import Point
from django.core.management import call_command


def initialize_db(apps, schema_editor):
    print('loading data...')
    call_command(
        'loaddata', 'fetch_brewery/fixtures/initial_brewery_data.json')


def deinitialize(apps, schema_editor):
    print('deinitializing')


def populate_point_fields(apps, schema_editor):
    Brewery = apps.get_model("breweries", "Brewery")
    db_alias = schema_editor.connection.alias

    for b in Brewery.objects.using(db_alias).all():
        if b.latitude is not None and b.longitude is not None:
            b.point = Point(x=b.longitude, y=b.latitude, srid=4326)
            b.save()


def reverse_point_fields(apps, schema_editor):
    Brewery = apps.get_model("breweries", "Brewery")
    db_alias = schema_editor.connection.alias
    Brewery.objects.using(db_alias).all().update(point=None)


class Migration(migrations.Migration):

    dependencies = [
        ('breweries', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(initialize_db, deinitialize),
        migrations.RunPython(populate_point_fields, reverse_point_fields),
    ]
