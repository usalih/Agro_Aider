from . import models
from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description')  # Fields to display in the list view
    search_fields = ('name', 'description')  # Fields to search
    list_filter = ('category',)  # Filters to use
    ordering = ('name',)  # Default ordering
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'category')
        }),
        ('Content', {
            'fields': ('article', 'video', 'file', 'image')
        }),
    )

admin.site.register(Product, ProductAdmin)

