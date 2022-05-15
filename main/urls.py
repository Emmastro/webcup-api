from main import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'location', views.LocationViewSet, basename='location')
router.register(r'textpackage', views.TextPackageViewSet, basename='textpackage')
router.register(r'imagepackage', views.ImagePackageViewSet, basename='imagepackage')
router.register(r'itempackage', views.ItemPackageViewSet, basename='itempackage')
router.register(r'audiopackage', views.AudioPackageViewSet, basename='audiopackage')
router.register(r'videopackage', views.VideoPackageViewSet, basename='videopackage')

urlpatterns = router.urls
