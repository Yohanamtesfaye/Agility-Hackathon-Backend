from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from report_app.models import Report
from .models import Notification

@receiver(post_save, sender=Report)
def handle_report_notifications(sender, instance, created, **kwargs):
    # Create notification
    notification_type = Notification.FILED_REPORT if created else Notification.REPORT_UPDATE
    message = (
        f"Thank you for your report on {instance.description}"
        if created
        else f"Update on your report: {instance.description}"
    )

    Notification.objects.create(
        user=instance.user,
        report=instance,
        message=message,
        notification_type=notification_type
    )

    # Send email
    subject = "Report Submitted" if created else "Report Updated"
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [instance.user.email],
        fail_silently=True  # Set to False in production
    )