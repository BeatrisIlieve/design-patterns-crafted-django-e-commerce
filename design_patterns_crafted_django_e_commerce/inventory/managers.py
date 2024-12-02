from django.db import (
    models,
)

from django.db.models import (
    Case,
    When,
    Value,
    CharField,
    Min,
    Max,
    Sum,
    BooleanField,
)

from django.contrib.postgres.aggregates import (
    JSONBAgg,
)

from django.db.models.functions import (
    JSONObject,
    Cast,
)

from design_patterns_crafted_django_e_commerce.utils.queries.get_full_category_title import (
    get_full_category_title,
)
from design_patterns_crafted_django_e_commerce.utils.queries.get_full_color_title import (
    get_full_color_title,
)


class InventoryManager(models.Manager):

    def get_product_into_products_list(self, category_pk, color_pk):
        result = (
            self.filter(
                product__category_id=category_pk,
                product__color_id=color_pk,
            )
            .select_related("product", "product__category", "product__color")
            .values(
                "product_id",
                "product__category_id",
                "product__color_id",
                "product__first_image_url",
                "product__second_image_url",
                full_category_title=get_full_category_title(),
                full_color_title=get_full_color_title(),
            )
            .annotate(
                min_price=Min("price"),
                max_price=Max("price"),
                total_quantity=Sum("quantity"),
                is_sold_out=Case(
                    When(total_quantity=0, then=Value("Sold Out")),
                    default=Value("In Stock"),
                    output_field=BooleanField(),
                ),
            ).order_by("pk")
        )

        return result

    def get_product_into_product_page(self, category_pk, color_pk):

        result = (
            self.filter(
                product__category_id=category_pk,
                product__color_id=color_pk,
            )
            .select_related("product", "product__category", "product__color")
            .values(
                "product_id",
                "product__category_id",
                "product__color_id",
                "product__first_image_url",
                "product__second_image_url",
                "product__description",
                full_category_title=get_full_category_title(),
                full_color_title=get_full_color_title(),
            )
            .annotate(
                inventory_details=JSONBAgg(
                    JSONObject(
                        inventory_id="id",
                        size="size",
                        price=Cast("price", output_field=CharField()),
                        stock_status=Case(
                            When(quantity=0, then=Value("Sold Out")),
                            default=Value("In Stock"),
                            output_field=CharField(),
                        ),
                    ),
                ),
                total_quantity=Sum("quantity"),
                is_sold_out=Case(
                    When(total_quantity=0, then=Value("Sold Out")),
                    default=Value("In Stock"),
                    output_field=BooleanField(),
                ),
            ).order_by("pk")
        )

        return result
