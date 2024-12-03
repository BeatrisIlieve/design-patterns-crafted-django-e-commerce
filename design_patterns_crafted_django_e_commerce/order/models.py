# from django.db import models

# from design_patterns_crafted_django_e_commerce.common.models.base_shopping_entity import (
#     BaseShoppingEntity,
# )

# from design_patterns_crafted_django_e_commerce.user_shipping_details.models import (
#     UserShippingDetails,
# )


# class Order(models.Model):
#     DELIVERY_METHOD_CHOICES = (
#         ("SP", "Store Pickup"),
#         ("EH", "Express Home Delivery"),
#         ("RH", "Regular Home Delivery"),
#     )

#     delivery_method = models.CharField(
#         max_length=2,
#         choices=DELIVERY_METHOD_CHOICES,
#         null=True,
#         blank=True,
#     )

#     delivery_cost = models.DecimalField(
#         max_digits=4,
#         decimal_places=2,
#         null=True,
#         blank=True,
#     )

#     total_cost = models.DecimalField(
#         max_digits=7,
#         decimal_places=2,
#         null=True,
#         blank=True,
#     )

#     due_date = models.DateField(
#         null=True,
#         blank=True,
#     )

#     user = models.ForeignKey(
#         to=UserShippingDetails,
#         on_delete=models.CASCADE,
#     )


# class OrderItem(BaseShoppingEntity):
#     class Meta:
#         unique_together = ("user", "inventory", "order")

#     order = models.ForeignKey(
#         to=Order,
#         on_delete=models.CASCADE,
#     )
