from django.urls import path, include
from rest_framework.routers import DefaultRouter
from order import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'', views.OrderViewSet,basename="order")

urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),       
]