from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Notification
from .serializers import NotificationSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recent_notifications(request):
    """Recent unread notifications (for bell icon)"""
    notifications = Notification.objects.filter(
        user=request.user,
        is_read=False
    ).order_by('-created_at')[:5]
    serializer = NotificationSerializer(notifications, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def all_notifications(request):
    """All notifications with filtering (for sidebar)"""
    notification_type = request.query_params.get('type')
    queryset = Notification.objects.filter(user=request.user)

    if notification_type in ['filed_report', 'report_update']:
        queryset = queryset.filter(notification_type=notification_type)

    serializer = NotificationSerializer(queryset.order_by('-created_at'), many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def mark_as_read(request, notification_id):
    """Mark notification as read"""
    notification = Notification.objects.get(id=notification_id, user=request.user)
    notification.is_read = True
    notification.save()
    return Response({'status': 'success'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def unread_count(request):
    """Get unread notifications count"""
    count = Notification.objects.filter(user=request.user, is_read=False).count()
    return Response({'unread_count': count})