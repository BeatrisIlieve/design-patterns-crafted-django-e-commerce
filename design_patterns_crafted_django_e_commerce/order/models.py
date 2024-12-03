from django.db import models

from design_patterns_crafted_django_e_commerce.common.models.base_shopping_entity import (
    BaseShoppingEntity,
)

from design_patterns_crafted_django_e_commerce.user_credential_details.models import (
    UserCredentialDetails,
)


class Order(models.Model):
    user = models.ForeignKey(
        to=UserCredentialDetails,
        on_delete=models.CASCADE,
    )

    def save(self, *args, **kwargs):
        self.clean()

        is_new = self.pk is None
        super().save(*args, **kwargs)

        if is_new:
            OrderItem.objects.create(user=self)


class OrderItem(BaseShoppingEntity):
    class Meta:
        unique_together = ("user", "inventory", "order")

    order = models.OneToOneField(
        to=Order,
        on_delete=models.CASCADE,
        primary_key=True,
    )
