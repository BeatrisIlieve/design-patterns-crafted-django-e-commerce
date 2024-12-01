from django.db import (
    models,
)

from design_patterns_crafted_django_e_commerce.user_credential_details.models import (
    UserCredentialDetails,
)
from design_patterns_crafted_django_e_commerce.inventory.models import (
    Inventory,
)


class InventoryItems(models.Model):
    quantity = models.PositiveIntegerField(
        default=1,
    )

    inventory = models.ForeignKey(
        to=Inventory,
        on_delete=models.CASCADE,
    )


class BaseShoppingEntity(models.Model):
    class Meta:
        abstract = True

    items = models.ForeignKey(
        to=InventoryItems,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        to=UserCredentialDetails,
        on_delete=models.CASCADE,
    )
