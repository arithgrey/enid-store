from django.urls import path, include
from rest_framework.routers import DefaultRouter
from lead_type import views

router = DefaultRouter()
router.register(r'', views.LeadTypeViewSet, basename="lead-type")

urlpatterns = [
    path('', include(router.urls)),
]