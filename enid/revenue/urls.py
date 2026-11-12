from django.urls import path
from revenue.views import (
    MonthlyRevenueView, SummaryRevenueView,
    ComparisonRevenueView, ByProductRevenueView,
)

urlpatterns = [
    path('monthly/', MonthlyRevenueView.as_view(), name='revenue-monthly'),
    path('summary/', SummaryRevenueView.as_view(), name='revenue-summary'),
    path('comparison/', ComparisonRevenueView.as_view(), name='revenue-comparison'),
    path('by-product/', ByProductRevenueView.as_view(), name='revenue-by-product'),
]
