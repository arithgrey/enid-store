from rest_framework.routers import DefaultRouter
from faqs import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'', views.FaqViewSet,basename="faq")
# The API URLs are now determined automatically by the router.
urlpatterns = router.urls