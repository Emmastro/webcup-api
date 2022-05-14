import logging

from .models import Location, TextPackage, ImagePackage, ItemPackage
from rest_framework import serializers


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'name')

class TextPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextPackage
        fields = ('id', 'client', 'location', 'text', 'medium')

class ImagePackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagePackage
        fields = ('id', 'client', 'location', 'image', 'medium')

class ItemPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPackage
        fields = ('id', 'client', 'location', 'name', 'size', 'weight')