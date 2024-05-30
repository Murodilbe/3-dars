from rest_framework import serializers
from .models import Hotel, Class, Travel
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser


class TravelSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()
    hotel_id = serializers.IntegerField()
    term = serializers.FloatField()
    klass_id = serializers.IntegerField()

    def create(self, validated_data):
        return Travel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.hotel_id = validated_data.get('hotel_id', instance.hotel_id)
        instance.term = validated_data.get('term', instance.term)
        instance.klass_id = validated_data.get('klass_id', instance.klass_id)
        instance.save()
        return instance


class ClassSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=65)
    price = serializers.IntegerField()

    def create(self, validated_data):
        return Class.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance

class HotelSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=150)
    stars = serializers.IntegerField()
    price = serializers.IntegerField()

    def create(self, validated_data):
        return Hotel.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.stars = validated_data.get('stars', instance.stars)
        instance.price = validated_data.get('price', instance.price)