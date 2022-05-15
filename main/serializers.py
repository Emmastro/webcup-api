import logging

from .models import Location, TextPackage, ImagePackage, ItemPackage, AudioPackage, VideoPackage
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


class AudioPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioPackage
        fields = ('id', 'client', 'location', 'audio', 'medium')

class VideoPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoPackage
        fields = ('id', 'client', 'location', 'video', 'medium')

class ItemPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPackage
        fields = ('id', 'client', 'location', 'name', 'size', 'weight')