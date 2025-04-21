from django.urls import path
from report_app.api.views import ReportList,ReportDetail

urlpatterns = [
    path("report",ReportList.as_view(),name="report"),
    path("report/<uuid:pk>",ReportDetail.as_view(),name="report_details")
]


