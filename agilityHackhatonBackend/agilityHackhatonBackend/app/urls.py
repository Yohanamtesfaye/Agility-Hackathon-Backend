# urls.py
from django.urls import path
from .views import (
    UserListCreateView, UserDetailView, CategoryListCreateView, CategoryDetailView,
    StatusListCreateView, StatusDetailView, ReportListCreateView, ReportDetailView,
    ReportVoteListCreateView, ReportVoteDetailView, NotificationListCreateView, NotificationDetailView,
    AuthorityAssignmentListCreateView, AuthorityAssignmentDetailView, AnalyticListCreateView, AnalyticDetailView
)

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list'),
    path('users/<uuid:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('categories/', CategoryListCreateView.as_view(), name='category-list'),
    path('categories/<uuid:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('statuses/', StatusListCreateView.as_view(), name='status-list'),
    path('statuses/<uuid:pk>/', StatusDetailView.as_view(), name='status-detail'),
    path('reports/', ReportListCreateView.as_view(), name='report-list'),
    path('reports/<uuid:pk>/', ReportDetailView.as_view(), name='report-detail'),
    path('report-votes/', ReportVoteListCreateView.as_view(), name='report-vote-list'),
    path('report-votes/<uuid:pk>/', ReportVoteDetailView.as_view(), name='report-vote-detail'),
    path('notifications/', NotificationListCreateView.as_view(), name='notification-list'),
    path('notifications/<uuid:pk>/', NotificationDetailView.as_view(), name='notification-detail'),
    path('authority-assignments/', AuthorityAssignmentListCreateView.as_view(), name='authority-assignment-list'),
    path('authority-assignments/<uuid:pk>/', AuthorityAssignmentDetailView.as_view(), name='authority-assignment-detail'),
    path('analytics/', AnalyticListCreateView.as_view(), name='analytic-list'),
    path('analytics/<uuid:pk>/', AnalyticDetailView.as_view(), name='analytic-detail'),
]