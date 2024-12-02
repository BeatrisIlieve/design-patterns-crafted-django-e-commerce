from django.db.models import (
    Case,
    When,
    Value,
    BooleanField,
)


def check_if_all_product_sizes_are_sold_out():
    return (
        Case(
            When(total_quantity=0, then=Value("Sold Out")),
            default=Value("In Stock"),
            output_field=BooleanField(),
        ),
    )
