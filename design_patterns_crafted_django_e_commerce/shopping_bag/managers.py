from django.db import (
    models,
)


class ShoppingBagManager(models.Manager):
    def add_or_update_item(self, user, inventory):
        shopping_bag_item, created = self.get_or_create(user=user, inventory=inventory)

        if not created:

            shopping_bag_item.quantity += 1
            shopping_bag_item.save()

        return shopping_bag_item
