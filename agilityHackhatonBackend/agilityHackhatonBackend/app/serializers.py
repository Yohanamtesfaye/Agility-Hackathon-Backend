# serializers.py
from rest_framework import serializers
from .models import User, Category, Status, Report, ReportVote, Notification, AuthorityAssignment, Analytic

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'phone_number', 'name', 'location', 'role', 'created_at', 'updated_at']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'created_at']

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id', 'name', 'description', 'created_at']

class ReportSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    status = StatusSerializer(read_only=True)

    class Meta:
        model = Report
        fields = ['id', 'user', 'category', 'description', 'severity', 'latitude', 'longitude', 'image_url', 'status', 'created_at', 'updated_at', 'resolved_at']
        read_only_fields = ['created_at', 'updated_at', 'resolved_at']

class ReportVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportVote
        fields = ['id', 'report', 'user', 'vote_type', 'created_at']
        read_only_fields = ['created_at']

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'user', 'report', 'message', 'type', 'is_read', 'created_at']
        read_only_fields = ['created_at']

class AuthorityAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorityAssignment
        fields = ['id', 'report', 'authority', 'assigned_at']
        read_only_fields = ['assigned_at']

class AnalyticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analytic
        fields = ['id', 'report', 'category', 'resolution_time', 'created_at']
        read_only_fields = ['created_at']