from django.db import models


from design_patterns_crafted_django_e_commerce.user_credential_details.models import (
    UserCredentialDetails,
)
from design_patterns_crafted_django_e_commerce.inventory.models import (
    Inventory,
)


class Order(models.Model):
    user = models.ForeignKey(
        to=UserCredentialDetails,
        on_delete=models.CASCADE,
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
    )


class OrderItem(models.Model):

    class Meta:
        unique_together = (
            "inventory",
            "order",
        )

    quantity = models.PositiveIntegerField()

    inventory = models.ForeignKey(
        to=Inventory,
        on_delete=models.CASCADE,
    )

    order = models.ForeignKey(
        to=Order,
        on_delete=models.CASCADE,
    )
    
