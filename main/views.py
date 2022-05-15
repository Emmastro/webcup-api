from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from main import models, serializers

class LocationViewSet(viewsets.ModelViewSet):
    queryset = models.Location.objects.all()
    serializer_class = serializers.LocationSerializer

    @action(detail=False, methods=['get'])
    def get_locations(self, request):
        locations = models.Location.objects.all()
        serializer = serializers.LocationSerializer(locations, many=True)
        return Response(serializer.data)
    
class TextPackageViewSet(viewsets.ModelViewSet):
    queryset = models.TextPackage.objects.all()
    serializer_class = serializers.TextPackageSerializer

    @action(detail=False, methods=['get'])
    def get_text_packages(self, request):
        text_packages = models.TextPackage.objects.all()
        serializer = serializers.TextPackageSerializer(text_packages, many=True)
        return Response(serializer.data)


class ImagePackageViewSet(viewsets.ModelViewSet):
    queryset = models.ImagePackage.objects.all()
    serializer_class = serializers.ImagePackageSerializer

    @action(detail=False, methods=['get'])
    def get_image_packages(self, request):
        image_packages = models.ImagePackage.objects.all()
        serializer = self.serializer_classs(image_packages, many=True)
        return Response(serializer.data)

class VideoPackageViewSet(viewsets.ModelViewSet):
    queryset = models.VideoPackage.objects.all()
    serializer_class = serializers.VideoPackageSerializer

    @action(detail=False, methods=['get'])
    def get_video_packages(self, request):
        video_packages = models.VideoPackage.objects.all()
        serializer = self.serializer_class(video_packages, many=True)
        return Response(serializer.data)

class AudioPackageViewSet(viewsets.ModelViewSet):
    queryset = models.AudioPackage.objects.all()
    serializer_class = serializers.AudioPackageSerializer

    @action(detail=False, methods=['get'])
    def get_audio_packages(self, request):
        audio_packages = models.AudioPackage.objects.all()
        serializer = self.serializer_class(audio_packages, many=True)
        return Response(serializer.data)


class ItemPackageViewSet(viewsets.ModelViewSet):
    queryset = models.ItemPackage.objects.all()
    serializer_class = serializers.ItemPackageSerializer

    @action(detail=False, methods=['get'])
    def get_item_packages(self, request):
        item_packages = models.ItemPackage.objects.all()
        serializer = serializers.ItemPackageSerializer(item_packages, many=True)
        return Response(serializer.data)

