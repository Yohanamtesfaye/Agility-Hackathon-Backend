from django.urls import path
from .views import AnalyticListView

urlpatterns = [
    path('analytics/', AnalyticListView.as_view(), name='analytic-list'),
]
