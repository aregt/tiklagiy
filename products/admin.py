from django.contrib import admin
from .models import Product, Category, ProductSize, ProductVariation

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'brand', 'category', 'season', 'created_at')
    list_filter = ('brand', 'category', 'season', 'fabric_type')
    search_fields = ('name', 'description', 'brand')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    search_fields = ('name',)

@admin.register(ProductSize)
class ProductSizeAdmin(admin.ModelAdmin):
    list_display = ('product', 'size', 'stock')
    list_filter = ('size',)
    search_fields = ('product__name',)

@admin.register(ProductVariation)
class ProductVariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'color')
    list_filter = ('color',)
    search_fields = ('product__name', 'color')