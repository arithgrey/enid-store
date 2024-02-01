from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'', views.userViewSet,basename="user")

urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),       
]