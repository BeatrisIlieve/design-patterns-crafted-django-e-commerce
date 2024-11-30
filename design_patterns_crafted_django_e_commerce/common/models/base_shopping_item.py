# from django.db import models


# class BaseShoppingItem(models.Model):
#     class Meta:
#         abstract = True
#         unique_together = ("user", "inventory")

#     objects = BaseShoppingItemManager()

#     quantity = models.PositiveIntegerField(
#         default=1,
#     )

#     inventory = models.ForeignKey(
#         to=Inventory,
#         on_delete=models.CASCADE,
#         related_name="inventory",
#     )

#     user = models.ForeignKey(
#         to=UserCredentialDetails,
#         on_delete=models.CASCADE,
#         related_name="user_shopping_bag",
#     )

#     @property
#     def total_price(self):
#         return BaseShoppingItem.objects.calculate_total_price(self.user)
