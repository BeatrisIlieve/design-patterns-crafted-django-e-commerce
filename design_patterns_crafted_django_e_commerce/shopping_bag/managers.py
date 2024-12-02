from django.db import (
    models,
)
from django.db.models import (
    Sum,
    F,
)

from design_patterns_crafted_django_e_commerce.inventory.models import (
    Inventory,
)


class ShoppingBagManager(models.Manager):
    def add_item(self, inventory_pk, user):
        inventory = Inventory.objects.get(pk=inventory_pk)

        shopping_bag_item, created = self.get_or_create(user=user, inventory=inventory)

        if not created:

            shopping_bag_item.quantity += 1
            shopping_bag_item.save()

            return "Shopping bag item quantity has been increased"
        
        return "Item has been added to shopping bag"
    
    def increase_item_quantity(self, inventory_pk, user):
        inventory = Inventory.objects.get(pk=inventory_pk)
        
        if inventory.quantity == 0:
            return "Not enough inventory quantity"
    
        self.filter(inventory=inventory, user=user).update(quantity=F("quantity") + 1)
        
        return "Quantity has been increased"
    
    def decrease_item_quantity(self, inventory_pk, user):
        inventory = Inventory.objects.get(pk=inventory_pk)
        
        shopping_bag_item = self.get(inventory=inventory, user=user)
        
        if shopping_bag_item.quantity == 0:
            return "Quantity has already reached zero"
    
        self.filter(inventory=inventory, user=user).update(quantity=F("quantity") - 1)
        
        return "Quantity has been increased"
        
        
    def calculate_total_price(self, user):
        total_price = (
            self.objects.filter(user=user)
            .annotate(item_total=F("quantity") * F("inventory__price"))
            .aggregate(total_price=Sum("item_total"))["total_price"]
        )

        return total_price
