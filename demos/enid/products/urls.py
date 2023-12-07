from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'producto', views.ProductVuewSet, basename="product")
router.register(r'item-card', views.ItemCardVuewSet, basename="itemcard")
router.register(r'card', views.CardVuewSet, basename="card")


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
