from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'lead_search'

urlpatterns = [
    path('', views.LeadSearchViewSet.as_view({'get': 'search'}), name='lead-search'),
]