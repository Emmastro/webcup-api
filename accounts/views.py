from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from accounts import models, serializers



class ClientViewSet(viewsets.ModelViewSet):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer

    # register client
    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = serializers.ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
