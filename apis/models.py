
from datetime import datetime

from django.db import models

# Create your models here.

#Company Details

class IndustrySector(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name

class Company(models.Model):

    name = models.CharField(max_length=50)
    wallet_address = models.CharField(max_length=50, unique = True)
    industry = models.ForeignKey(IndustrySector,blank= False,null=False, on_delete=models.CASCADE)
    website = models.TextField()

    def __str__(self) -> str:
        return self.name

#Footprint Details

class FootprintReport(models.Model):

    REPORTING_CHOICES = (("MONTH","Month"),("YEAR", "Year"))

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    reporting_period = models.CharField(max_length=10, choices=REPORTING_CHOICES, default= "Month")
    total_emission = models.FloatField()
    timestamp = models.DateTimeField(default= datetime.now)
    transaction_hash = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.company.name + "'s footprint at"


class FootprintBreakdown(models.Model):

    footprint = models.OneToOneField(FootprintReport, on_delete= models.CASCADE)
    scope1_emission = models.FloatField()
    scope2_emission = models.FloatField()
    scope3_emission = models.FloatField()

    def __str__(self) -> str:
        return "breakdown"+ self.footprint.company.name

class FootprintSource(models.Model):
    breakdown = models.ForeignKey(FootprintBreakdown, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    emissions = models.FloatField()

    def __str__(self) -> str:
        return self.name


#Intiatives

class GreenInitiatives(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    description = models.TextField()
    impact_area = models.CharField(max_length=250)

    def __str__(self) -> str:
        return "initiative " + self.company.name
