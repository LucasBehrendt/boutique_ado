from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Configuration for Category table on admin page"""
    list_display = (
        'friendly_name',
        'name',
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Configuration for Product table on admin page"""
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )
    ordering = ('sku', )
