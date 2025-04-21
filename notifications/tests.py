
from django.test import TestCase
from django.contrib.auth import get_user_model
from report_app.models import Report
from .models import Notification

User = get_user_model()

class NotificationTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="test@example.com",
            name="Test User",
            password="testpass123"
        )
        self.report = Report.objects.create(
            user=self.user,
            description="Pothole on Main Road",
            severity=1,
            latitude=6.5244,
            longitude=3.3792,
            image_url="http://example.com/image.jpg"
        )

    def test_notification_creation_on_submit(self):
        self.assertEqual(Notification.objects.count(), 1)
        notification = Notification.objects.first()
        self.assertEqual(notification.notification_type, 'filed_report')
        self.assertIn("Thank you for your report", notification.message)

    def test_notification_creation_on_update(self):
        self.report.description = "Updated description"
        self.report.save()
        self.assertEqual(Notification.objects.count(), 2)
        notification = Notification.objects.last()
        self.assertEqual(notification.notification_type, 'report_update')
        self.assertIn("Update on your report", notification.message)