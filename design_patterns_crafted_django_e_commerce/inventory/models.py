from django.db import models
from django.core.validators import (
    MaxValueValidator,
)

from design_patterns_crafted_django_e_commerce.product.models import (
    Product,
)


class Inventory(models.Model):

    class Meta:
        unique_together = ("product", "size")
        verbose_name_plural = "Inventories"

    quantity = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(
                3, message="The maximum quantity per product inventory is 3."
            ),
        ]
    )

    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        related_name="product_inventory",
    )

    size = models.DecimalField(
        max_digits=4,
        decimal_places=2,
    )

    price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
    )

    created_at = models.DateField(
        auto_now_add=True,
    )

    updated_at = models.DateField(
        auto_now=True,
    )

    @property
    def is_sold_out(self):
        return self.quantity <= 0
