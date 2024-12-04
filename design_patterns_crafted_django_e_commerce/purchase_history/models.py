from django.db import (
    models,
)

from design_patterns_crafted_django_e_commerce.user_credential_details.models import (
    UserCredentialDetails,
)
from design_patterns_crafted_django_e_commerce.user_delivery.models import (
    Delivery,
)
from design_patterns_crafted_django_e_commerce.order.models import (
    OrderItem,
)


class PurchaseHistory(models.Model):
    user = models.ForeignKey(
        to=UserCredentialDetails,
        on_delete=models.CASCADE,
    )

    delivery = models.ForeignKey(
        to=Delivery,
        on_delete=models.CASCADE,
    )

    order_item = models.ForeignKey(
        to=OrderItem,
        on_delete=models.CASCADE,
    )
