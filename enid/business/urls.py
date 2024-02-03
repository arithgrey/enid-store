from django.urls import path, include
from rest_framework.routers import DefaultRouter
from business.views import BusinessSlugImagesViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'business', BusinessSlugImagesViewSet, basename='business')

urlpatterns = [
    path('<str:business_slug>/imagenes-referencia/', BusinessSlugImagesViewSet.as_view({'get':'images_by_slug'}), name='business_images'),
    path('', include(router.urls)),
]