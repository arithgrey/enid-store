from django.urls import path, include
from rest_framework.routers import DefaultRouter
from returns import views

router = DefaultRouter()
router.register(r'', views.ReturnsViewSet,basename="returns")
# The API URLs are now determined automatically by the router.
urlpatterns = router.urls