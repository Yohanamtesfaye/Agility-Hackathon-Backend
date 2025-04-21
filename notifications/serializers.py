from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    report_image_url = serializers.CharField(source='report.image_url', read_only=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%SZ")

    class Meta:
        model = Notification
        fields = [
            'id', 
            'message', 
            'notification_type', 
            'is_read', 
            'created_at',
            'report_image_url'
        ]