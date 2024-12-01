from django.db import models

from .managers import (
    WishlistManager,
)

from design_patterns_crafted_django_e_commerce.product.models import (
    Product,
)
from design_patterns_crafted_django_e_commerce.user_credential_details.models import (
    UserCredentialDetails,
)


class Wishlist(models.Model):
    class Meta:
        unique_together = (
            "user",
            "product",
        )
        
    objects = WishlistManager()

    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        to=UserCredentialDetails,
        on_delete=models.CASCADE,
    )
