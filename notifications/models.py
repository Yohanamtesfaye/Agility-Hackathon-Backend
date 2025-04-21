from django.db import models
from django.conf import settings

class Notification(models.Model):
    FILED_REPORT = 'filed_report'
    REPORT_UPDATE = 'report_update'
    TYPE_CHOICES = [
        (FILED_REPORT, 'Filed Report'),
        (REPORT_UPDATE, 'Report Update'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='notifications'
    )
    report = models.ForeignKey(
        'report_app.Report',  # Reference to the Report model in the other app
        on_delete=models.CASCADE
    )
    message = models.TextField()
    notification_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.email}: {self.message[:30]}"