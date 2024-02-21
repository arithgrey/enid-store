from django.urls import path
from logout.views import LogoutView

urlpatterns = [    
    path('logout/', LogoutView.as_view(), name='logout'),
]