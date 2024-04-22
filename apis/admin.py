from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Company)
admin.site.register(FootprintReport)
admin.site.register(FootprintBreakdown)
admin.site.register(FootprintSource)
admin.site.register(GreenInitiatives)

