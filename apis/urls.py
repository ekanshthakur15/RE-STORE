from django.urls import path

from .views import *

urlpatterns = [
    path('industry-sectors/', IndustrySectorListAPIView.as_view(), name='industry_sector'),
    path('companies/', CompanyListAPIView.as_view()),
    path("companies/details/<str:wallet_address>/",CompanyDetailView.as_view(), name="company_detail"),
    path("companies/exists/<str:wallet_address>/",CompanyExistsAPIView.as_view(), name="company_exist"),
    path('footprint-reports/', FootprintReportList.as_view(), name='footprint_report'),
    path('footprint-reports/<str:wallet_address>/', FootprintReportList.as_view(), name='footprint_report'),
    path('footprint-breakdowns/', FootprintBreakdownList.as_view(), name='footprint_breakdown'),
    path('footprint-breakdowns/<int:footprint_id>', FootprintBreakdownList.as_view(), name='footprint_breakdown_details'),
    path('footprint-sources/', FootprintSourceList.as_view(), name='footprint_source'),
]
