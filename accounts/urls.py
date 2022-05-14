#from . import views
#from rest_framework.routers import DefaultRouter
from django.urls import include, path


#router = DefaultRouter()

urlpatterns = [
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls'))
]

#router.register(r'register', views.ClientViewSet, basename='register')

#urlpatterns = router.urls

