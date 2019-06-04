from django.contrib import admin
from .models import QuoteRecord, PropertyData

# Register your models here.
admin.site.register(QuoteRecord)
admin.site.register(PropertyData)
