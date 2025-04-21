from rest_framework import serializers
from .models import Analytic, Category, Report, Status

class AnalyticSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    user_username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Analytic
        fields = [
            'id', 'category', 'category_name', 'user', 'user_username',
            'average_resolution_time', 'report_count', 'last_updated'
        ]

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['id', 'title', 'description', 'user', 'category', 'status', 'created_at', 'resolved_at']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id', 'name']
