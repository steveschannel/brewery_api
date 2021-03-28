from django.contrib.gis.db import models


class Brewery(models.Model):

    name = models.CharField(max_length=100, null=False)
    brewery_type = models.CharField(max_length=20, null=False)

    street = models.CharField(max_length=100, null=True)
    address_2 = models.CharField(max_length=100, null=True)
    address_3 = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=False)
    state = models.CharField(max_length=100, null=False)
    county_province = models.CharField(max_length=100, null=False)
    postal_code = models.CharField(max_length=20, default="07302")
    website_url = models.URLField()

    phone = models.CharField(max_length=11, null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    country = models.CharField(max_length=100, null=False)

    longitude = models.FloatField(
        default=None, null=True
    )
    latitude = models.FloatField(
        default=None, null=True
    )

    point = models.PointField(geography=True, default=None, null=True)
    tags = models.CharField(max_length=100, null=True)
