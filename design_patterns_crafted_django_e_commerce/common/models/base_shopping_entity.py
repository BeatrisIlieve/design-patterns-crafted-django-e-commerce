from django.db import (
    models,
)

from design_patterns_crafted_django_e_commerce.user_credential_details.models import (
    UserCredentialDetails,
)
from design_patterns_crafted_django_e_commerce.inventory.models import (
    Inventory,
)


class BaseShoppingEntity(models.Model):
    class Meta:
        abstract = True
        unique_together = ("user", "inventory")

    quantity = models.PositiveIntegerField(
        default=1,
    )

    inventory = models.ForeignKey(
        to=Inventory,
        on_delete=models.CASCADE,
        related_name="inventory",
    )

    user = models.ForeignKey(
        to=UserCredentialDetails,
        on_delete=models.CASCADE,
        related_name="user_shopping_bag",
    )
