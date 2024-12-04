from django.db import models


from design_patterns_crafted_django_e_commerce.user_credential_details.models import (
    UserCredentialDetails,
)
from design_patterns_crafted_django_e_commerce.inventory.models import (
    Inventory,
)


class Order(models.Model):
    user = models.ForeignKey(
        to=UserCredentialDetails,
        on_delete=models.CASCADE,
    )

    def save(self, *args, **kwargs):
        is_new = self.pk is None

        super().save(*args, **kwargs)

        if is_new:
            OrderItem.objects.create(order=self)


class OrderItem(models.Model):

    class Meta:
        unique_together = (
            "inventory",
            "order",
        )

    quantity = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    inventory = models.ForeignKey(
        to=Inventory,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    order = models.OneToOneField(
        to=Order,
        on_delete=models.CASCADE,
        primary_key=True,
    )
