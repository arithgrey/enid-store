from django.urls import path, include
from rest_framework.routers import DefaultRouter
from variants import views

router = DefaultRouter()

router.register(r'', views.VariantVuewSet,basename="variant")

urlpatterns = [
    path('', include(router.urls)),
]