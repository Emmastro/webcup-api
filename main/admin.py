from django.contrib import admin

from .models import*

admin.site.register(Location)
admin.site.register(TextPackage)
admin.site.register(ImagePackage)
admin.site.register(ItemPackage)
admin.site.register(AudioPackage)
admin.site.register(VideoPackage)
