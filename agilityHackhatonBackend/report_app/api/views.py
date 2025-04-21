
from report_app.models import Report
from report_app.api.serializer import ReportSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters



class ReportList(generics.ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class =ReportSerializer
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['user_id', 'category_id','status']


class ReportDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer