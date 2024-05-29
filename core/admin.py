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
            'fields': ('name', 'description', 'category', 'image',)
        }),
        ('Content', {
            'fields': ('article', 'video', 'file')
        }),
    )

admin.site.register(Product, ProductAdmin)

from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_no','message', 'created_at',)
    search_fields = ('full_name', 'email', 'phone_no')
    list_filter = ('created_at',)
