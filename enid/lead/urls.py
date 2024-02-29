from django.urls import path, include
from rest_framework.routers import DefaultRouter
from lead import views

router = DefaultRouter()
router.register(r'', views.LeadViewSet, basename="lead")

urlpatterns = [
    path('', include(router.urls)),    
]