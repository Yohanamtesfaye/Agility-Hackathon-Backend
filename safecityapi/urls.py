from django.urls import path
from . import views
# 

urlpatterns = [
    path("user/register/",views.createUserList, name="user-register"),
    path("users/<int:pk>/",views.user_detail, name="user-detail"),
    path("statuses/", views.createStatusList, name="create-staus-list"),
    path("statuses/<int:pk>/", views.status_detail, name="status-detail"),
]
