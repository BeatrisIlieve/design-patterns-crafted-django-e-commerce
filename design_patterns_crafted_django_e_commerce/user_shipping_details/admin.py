from django.contrib import admin

from design_patterns_crafted_django_e_commerce.user_shipping_details.models import (
    UserShippingDetails,
)


@admin.register(UserShippingDetails)
class UserShippingDetailsAdmin(admin.ModelAdmin):
    pass
