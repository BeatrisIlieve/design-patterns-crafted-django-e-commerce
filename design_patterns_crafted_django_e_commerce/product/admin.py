from django.contrib import admin

from .models import (
    Product,
)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_filter = ("color", "category")

    fieldsets = (
        ("Details", {"fields": ("category", "color", "description")}),
        (
            "Images",
            {
                "fields": ("first_image_url", "second_image_url"),
                "classes": ("collapse",),
            },
        ),
    )
