from django.contrib import admin

from .models import (
    Inventory,
)


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):

    list_display = (
        "product",
        "quantity",
        "price",
        "size",
        "created_at",
        "updated_at",
    )

    list_filter = ("quantity", "price", "size")
