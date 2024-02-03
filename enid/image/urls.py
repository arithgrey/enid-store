from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from image import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'', views.ImageViewSet,basename="images")
# The API URLs are now determined automatically by the router.

urlpatterns = [
    path('', include(router.urls)),
]
