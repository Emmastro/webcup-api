from main import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'location', views.LocationViewSet, basename='location')
router.register(r'textpackage', views.TextPackageViewSet, basename='textpackage')
router.register(r'imagapackage', views.ImagePackageViewSet, basename='imagepackage')
router.register(r'itempackage', views.ItemPackageViewSet, basename='itempackage')

urlpatterns = router.urls
