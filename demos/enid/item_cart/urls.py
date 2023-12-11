from django.urls import path, include
from rest_framework.routers import DefaultRouter
from item_cart import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'', views.ItemCartVuewSet,basename="item-cart")
# The API URLs are now determined automatically by the router.
urlpatterns = router.urls