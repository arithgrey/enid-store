from django.urls import path
from revenue.views import MonthlyRevenueView, SummaryRevenueView

urlpatterns = [
    path('monthly/', MonthlyRevenueView.as_view(), name='revenue-monthly'),
    path('summary/', SummaryRevenueView.as_view(), name='revenue-summary'),
]
