from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api-auth/', include('rest_framework.urls')),
    path('api/', include('main.urls')),
    path('', include('accounts.urls')),
]
