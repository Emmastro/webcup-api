from django.db import models
from accounts.models import Client


class Location(models.Model):
    name = models.CharField(max_length=50)

class Package(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

class TextPackage(Package):
    text = models.TextField() # the text that will need to be printed and set to the selected location
    medium = models.CharField(max_length=50) # what the user wants the text to be printed on

class ImagePackage(Package):
    image = models.ImageField()
    medium = models.CharField(max_length=50) # what the user wants the image to be printed on

class ItemPackage(Package):

    # TODO: review input fields
    name = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    weight = models.IntegerField()
