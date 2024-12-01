from django.db import (
    models,
)
from django.db.models import (
    Sum,
    F,
)


class ShoppingBagManager(models.Manager):
    def add_or_update_item(self, user, inventory):
        shopping_bag_item, created = self.get_or_create(user=user, inventory=inventory)

        if not created:

            shopping_bag_item.quantity += 1
            shopping_bag_item.save()

        return shopping_bag_item
    
        
    def calculate_total_price(self, user):
        total_price = (
            self.objects.filter(user=user)
            .annotate(item_total=F("quantity") * F("inventory__price"))
            .aggregate(total_price=Sum("item_total"))["total_price"]
        )

        return total_price
