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
        serializer = serializers.ImagePackageSerializer(image_packages, many=True)
        return Response(serializer.data)

class ItemPackageViewSet(viewsets.ModelViewSet):
    queryset = models.ItemPackage.objects.all()
    serializer_class = serializers.ItemPackageSerializer

    @action(detail=False, methods=['get'])
    def get_item_packages(self, request):
        item_packages = models.ItemPackage.objects.all()
        serializer = serializers.ItemPackageSerializer(item_packages, many=True)
        return Response(serializer.data)

