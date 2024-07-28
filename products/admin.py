from django.contrib import admin
from .models import Product, Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'brand', 'category', 'season', 'created_at')
    list_filter = ('brand', 'category', 'season', 'fabric_type')
    search_fields = ('name', 'description', 'brand')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    search_fields = ('name',)