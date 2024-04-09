from . import models
from django.contrib import admin


class ProductImagesAdmin(admin.TabularInline):
    extra, model = 0, models.ProductImages


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    list_display = [
        "user",
        "title",
        "product_image",
        "pid",
    ]


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "category_image"]


@admin.register(models.ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ["full_name", "email", "phone_no", "message"]

