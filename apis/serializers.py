from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import *


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"

class IndustrySectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndustrySector
        fields = "__all__"

class FootPrintReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = FootprintReport
        fields = "__all__"

class FootprintBreakdownSerializer(serializers.ModelSerializer):
    class Meta:
        model = FootprintBreakdown
        fields = "__all__"


class FootprintSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FootprintSource
        fields = "__all__"

class GreenInitiativesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GreenInitiatives
        fields = "__all__"