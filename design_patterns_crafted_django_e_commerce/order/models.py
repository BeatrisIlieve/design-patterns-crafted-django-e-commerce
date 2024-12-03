from django.db import models

from design_patterns_crafted_django_e_commerce.user_credential_details.models import (
    UserCredentialDetails,
)

from design_patterns_crafted_django_e_commerce.common.models.base_shopping_entity import (
    BaseShoppingEntity,
)


class Order(models.Model):
    DELIVERY_METHOD_CHOICES = (
        ("SP", "Store Pickup"),
        ("EH", "Express Home Delivery"),
        ("RH", "Regular Home Delivery"),
    )
    
    delivery_method = models.CharField(
        max_length=2,
        choices=DELIVERY_METHOD_CHOICES,
    )

    delivery_cost = models.DecimalField(
        max_digits=4,
        decimal_places=2,
    )

    total_cost = models.DecimalField(
        max_digits=7,
        decimal_places=2,
    )

    due_date = models.DateField()

    user = models.ForeignKey(
        to=UserCredentialDetails,
        on_delete=models.CASCADE,
    )


class OrderItem(BaseShoppingEntity):
    order = models.ForeignKey(
        to=Order,
        on_delete=models.CASCADE,
    )
