from report_app.models import Report
from rest_framework import serializers

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model=Report
        fields="__all__"
        read_only_fields = ["id"]
