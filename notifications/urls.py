from django.urls import path
from . import views

urlpatterns = [
    path('notifications/recent/', views.recent_notifications),
    path('notifications/all/', views.all_notifications),
    path('notifications/mark-read/<uuid:notification_id>/', views.mark_as_read),
    path('notifications/unread-count/', views.unread_count),
]