from django.db import (
    models,
)

from django.db.models import (
    Case,
    When,
    Value,
    CharField,
)

from django.contrib.postgres.aggregates import (
    JSONBAgg,
)

from django.db.models.functions import (
    JSONObject,
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
                "product__description",
                full_category_title=Case(
                    When(product__category__title="E", then=Value("Earrings")),
                    When(product__category__title="B", then=Value("Bracelets")),
                    When(product__category__title="N", then=Value("Necklaces")),
                    When(product__category__title="R", then=Value("Rings")),
                    default=Value("Unknown Category"),
                    output_field=CharField(),
                ),
                full_color_title=Case(
                    When(product__color__title="P", then=Value("Pink")),
                    When(product__color__title="B", then=Value("Blue")),
                    When(product__color__title="W", then=Value("White")),
                    default=Value("Unknown Color"),
                    output_field=CharField(),
                ),
            )
            .annotate(
                inventory_details=JSONBAgg(
                    JSONObject(
                        inventory_id="id",
                        size="size",
                        price="price",
                        stock_status=Case(
                            When(quantity=0, then=Value("Sold Out")),
                            default=Value("In Stock"),
                            output_field=CharField(),
                        ),
                    ),
                )
            )
        )

        return result

    def get_product_into_product_page(self):
        pass
