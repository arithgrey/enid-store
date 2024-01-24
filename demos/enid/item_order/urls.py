from django.urls import path, include
from rest_framework.routers import DefaultRouter
from item_order import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'', views.ItemOrderViewSet,basename="item-order")
# The API URLs are now determined automatically by the router.
urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),       
]