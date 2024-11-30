from django.db import (
    models,
)
from django.db.models import (
    Sum,
)


class InventoryManager(models.Manager):
    def check_if_a_product_has_been_sold_out(self, category_pk, color_pk):
        return not self.filter(
            product__category_id=category_pk, product__color_id=color_pk
        ).aggregate(total_quantity=Sum("quantity"))["total_quantity"]
