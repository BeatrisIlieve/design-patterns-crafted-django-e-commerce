from decimal import (
    Decimal,
)

from design_patterns_crafted_django_e_commerce.shopping_bag.models import (
    ShoppingBag,
)


def calculate_total_delivery_cost(user, delivery_cost):
    shopping_bag_total_price = ShoppingBag.objects.calculate_total_price(user)

    delivery_cost = Decimal(delivery_cost)

    total_cost = shopping_bag_total_price + delivery_cost

    return total_cost
