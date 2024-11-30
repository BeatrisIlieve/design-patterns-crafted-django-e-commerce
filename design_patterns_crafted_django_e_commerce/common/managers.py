from django.db import (
    models,
)
from django.db.models import (
    Sum,
    F,
)


class BaseShoppingItemManager(models.Manager):
    def calculate_total_price(self, user):
        total_price = (
            self.objects.filter(user=user)
            .annotate(item_total=F("quantity") * F("inventory__price"))
            .aggregate(total_price=Sum("item_total"))["total_price"]
        )

        return total_price
