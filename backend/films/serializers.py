from rest_framework import serializers
from .models import *


class FilmSerializer(serializers.Serializer):
    poster = serializers.ImageField(source='poster.url')
    title_ru = serializers.CharField(max_length=255)
    title_orig = serializers.CharField(max_length=255)
    rating = serializers.FloatField()
    prod_year = serializers.IntegerField()
    timing = serializers.IntegerField()
    premiere_date = serializers.DateField()
    country_id = serializers.IntegerField()
    genre_id = serializers.IntegerField()
    director_id = serializers.IntegerField()