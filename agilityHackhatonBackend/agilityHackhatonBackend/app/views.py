# views.py
from rest_framework import generics, permissions
from .models import User, Category, Status, Report, ReportVote, Notification, AuthorityAssignment, Analytic
from .serializers import (
    UserSerializer, CategorySerializer, StatusSerializer, ReportSerializer,
    ReportVoteSerializer, NotificationSerializer, AuthorityAssignmentSerializer, AnalyticSerializer
)

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

class StatusListCreateView(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [permissions.IsAuthenticated]

class StatusDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [permissions.IsAuthenticated]

class ReportListCreateView(generics.ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ReportDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated]

class ReportVoteListCreateView(generics.ListCreateAPIView):
    queryset = ReportVote.objects.all()
    serializer_class = ReportVoteSerializer
    permission_classes = [permissions.IsAuthenticated]

class ReportVoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReportVote.objects.all()
    serializer_class = ReportVoteSerializer
    permission_classes = [permissions.IsAuthenticated]

class NotificationListCreateView(generics.ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

class NotificationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

class AuthorityAssignmentListCreateView(generics.ListCreateAPIView):
    queryset = AuthorityAssignment.objects.all()
    serializer_class = AuthorityAssignmentSerializer
    permission_classes = [permissions.IsAuthenticated]

class AuthorityAssignmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AuthorityAssignment.objects.all()
    serializer_class = AuthorityAssignmentSerializer
    permission_classes = [permissions.IsAuthenticated]

class AnalyticListCreateView(generics.ListCreateAPIView):
    queryset = Analytic.objects.all()
    serializer_class = AnalyticSerializer
    permission_classes = [permissions.IsAuthenticated]

class AnalyticDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Analytic.objects.all()
    serializer_class = AnalyticSerializer
    permission_classes = [permissions.IsAuthenticated]