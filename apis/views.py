from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *

# Create your views here.

class IndustrySectorListAPIView(APIView):

    def get(self, request):
        
        sectors = IndustrySector.objects.all()
        serializer = IndustrySectorSerializer(sectors, many=True)
        return Response(serializer.data)
    
    def post(self,request , format = None):

        serializer = IndustrySectorSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Industry created successfully"},status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

from django.shortcuts import get_object_or_404


class CompanyListAPIView(APIView):

    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        wallet_address = request.data.get("wallet_address")
        industry_id = request.data.get("industry")

        # Check if a company with the given wallet address already exists
        if Company.objects.filter(wallet_address=wallet_address).exists():
            return Response({"error": "Wallet address already used"}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the industry exists
        industry = get_object_or_404(IndustrySector, pk=industry_id)

        serializer = CompanySerializer(data=request.data)

        if serializer.is_valid():
            # Save the company with the associated industry
            serializer.save(industry=industry)
            return Response({"message": "Company created successfully"}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CompanyDetailView(APIView):
    
    def get(self, request, wallet_address):
        try:
            company = Company.objects.get(wallet_address=wallet_address)
            company_serializer = CompanySerializer(company)
        except Company.DoesNotExist:
            return Response({"error": "Company not found"}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            industry_sector = IndustrySector.objects.get(id=company.industry_id)
            industry_serializer = IndustrySectorSerializer(industry_sector)
        except IndustrySector.DoesNotExist:
            return Response({"error": "Industry sector not found"}, status=status.HTTP_404_NOT_FOUND)
        
        response_data = {
            "company": company_serializer.data,
            "industry_sector": industry_serializer.data
        }
        return Response(response_data, status=status.HTTP_200_OK)
        

class CompanyExistsAPIView(APIView):

    def get(self, request, wallet_address):

        company = Company.objects.filter(wallet_address=wallet_address).first()
        if company:
            return Response({"response":True}, status=status.HTTP_200_OK)
        else:
            return Response({"response":False}, status=status.HTTP_200_OK)

        
class FootprintReportList(APIView):

    def get(self, request,wallet_address):

        try:
            company = Company.objects.get(wallet_address = wallet_address)
        except Company.DoesNotExist:
            return Response({"error":"Company doesn't exist"},status=status.HTTP_404_NOT_FOUND)
        
        reports = FootprintReport.objects.filter(company = company)

        serializer = FootPrintReportSerializer(reports, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        company_id = request.data.get('company')

        try:
            company = Company.objects.get(pk = company_id)
            
        except Company.DoesNotExist:
            return Response({"error":"Company doesn't exist"},status=status.HTTP_404_NOT_FOUND)

        serializer = FootPrintReportSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(company = company)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FootprintBreakdownList(APIView):
    def get(self, request, footprint_id):

        try:
            footprint = FootprintReport.objects.get(pk = footprint_id)
        except FootprintReport.DoesNotExist:
            return Response({"error":"Footprint doesn't exist"}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            breakdown = FootprintBreakdown.objects.filter(footprint = footprint)
        except FootprintBreakdown.DoesNotExist:
            return Response({"error":"Breakdown doesn't exist"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = FootprintBreakdownSerializer(breakdown, many = True)
        return Response(serializer.data, status= status.HTTP_200_OK)

    def post(self, request):
        footprint_id = request.data.get('footprint')
        try:
            footprint = FootprintReport.objects.get(pk = footprint_id)
        except FootprintReport.DoesNotExist:
            return Response({"error":"Footprint Report doesn't exist"},status=status.HTTP_404_NOT_FOUND)

        serializer = FootprintBreakdownSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(footprint = footprint)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FootprintSourceList(APIView):
    def get(self, request, breakdown_id):

        try:
            query_set = FootprintSource.objects.get(breakdown = breakdown_id)
        except FootprintSource.DoesNotExist:
            return Response({"error":"Source List doesn't exist"}, status=status.HTTP_404_NOT_FOUND)
            
        serializer = FootprintSourceSerializer(query_set, many=True)
        return Response(serializer.data)

    def post(self, request):

        serializer = FootprintSourceSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)