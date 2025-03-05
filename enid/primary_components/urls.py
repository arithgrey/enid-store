from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductComponentViewSet

router = DefaultRouter()
router.register(r'components', ProductComponentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]