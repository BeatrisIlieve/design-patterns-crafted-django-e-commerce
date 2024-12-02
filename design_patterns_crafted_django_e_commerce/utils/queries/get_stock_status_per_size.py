from django.db.models import (
    Case,
    When,
    Value,
    CharField,
)


def get_stock_status_per_size():
    return Case(
        When(inventory__quantity=0, then=Value("Cannot Increase")),
        default=Value("Can Increase"),
        output_field=CharField(),
    )
