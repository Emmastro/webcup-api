from django.db import models
from accounts.models import Client


class Location(models.Model):
    name = models.CharField(max_length=50)


class Package(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)


class TextPackage(Package):
    # the text that will need to be printed and set to the selected location
    text = models.TextField()
    # what the user wants the text to be printed on
    medium = models.CharField(max_length=50)


class ImagePackage(Package):
    image = models.ImageField(upload_to="media/images")
    medium = models.CharField(max_length=50)


class AudioPackage(Package):
    audio = models.FileField(upload_to='media/audio/')
    medium = models.CharField(max_length=50)


class VideoPackage(Package):
    video = models.FileField(upload_to='media/videos/')
    medium = models.CharField(max_length=50)


class ItemPackage(Package):

    # TODO: review input fields
    name = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    weight = models.IntegerField()
