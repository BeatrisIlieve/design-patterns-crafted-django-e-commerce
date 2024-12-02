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
        shopping_bag_item = self.filter(inventory__pk=inventory_pk, user=user).first()

        if not shopping_bag_item:
            return "Item not found in the bag"

        shopping_bag_item.quantity -= 1
        shopping_bag_item.save()

        if shopping_bag_item.quantity == 0:
            shopping_bag_item.delete()
            return "Bag item has been deleted"

        return "Quantity has been decreased"

    def calculate_total_price(self, user):
        total_price = (
            self.objects.filter(user=user)
            .annotate(item_total=F("quantity") * F("inventory__price"))
            .aggregate(total_price=Sum("item_total"))["total_price"]
        )

        return total_price

    def get_all_shopping_bag_items_per_user(self, user):
        bag_items = (
            self.filter(user=user)
            .select_related("inventory", "inventory__product")
            .values("inventory__product__first_image_url", "inventory__size")
        )

        return bag_items
