from django.contrib import admin

from design_patterns_crafted_django_e_commerce.user_payment_details.models import (
    UserPaymentDetails,
)


@admin.register(UserPaymentDetails)
class UserPaymentDetailsAdmin(admin.ModelAdmin):
    pass
