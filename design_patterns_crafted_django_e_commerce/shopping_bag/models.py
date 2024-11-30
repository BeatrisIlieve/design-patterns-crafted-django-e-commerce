from .managers import (
    ShoppingBagManager,
)

from design_patterns_crafted_django_e_commerce.common.models.base_shopping_item import (
    BaseShoppingItem,
)


class ShoppingBag(BaseShoppingItem):

    objects = ShoppingBagManager()
