from django.db import (
    models,
)

from design_patterns_crafted_django_e_commerce.order.models import (
    Order,
)


class Delivery(models.Model):
    METHOD_CHOICES = (
        ("SP", "Store Pickup"),
        ("EH", "Express Home Delivery"),
        ("RH", "Regular Home Delivery"),
    )

    method = models.CharField(
        max_length=2,
        choices=METHOD_CHOICES,
    )

    total_cost = models.DecimalField(
        max_digits=7,
        decimal_places=2,
    )

    due_date = models.DateField()

    order = models.ForeignKey(
        to=Order,
        on_delete=models.CASCADE,
    )
