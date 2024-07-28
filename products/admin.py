from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'brand', 'season', 'created_at')
    list_filter = ('brand', 'season', 'fabric_type')
    search_fields = ('name', 'description', 'brand')