# WITH ordered_inventory AS (
#     SELECT
#         inv.id AS inventory_id,
#         inv.size,
#         inv.price,
#         inv.quantity,
#         inv.product_id
#     FROM
#         inventory_inventory AS inv
#     ORDER BY
#         inv.product_id, inv.size ASC
# )
# SELECT
#     prd.first_image_url,
#     prd.second_image_url,
#     prd.description,
#     pcat.title AS category,
#     pcol.title AS color,
#     STRING_AGG(
#         CONCAT_WS(
#             ';',
#             CONCAT('inventory_id', ':', oi.inventory_id),
#             CONCAT('size', ':', oi.size),
#             CONCAT('price', ':', oi.price),
#             CASE
#                 WHEN oi.quantity = 0 THEN 'Sold Out'
#                 ELSE 'In Stock'
#             END
#         ), ', '
#         ORDER BY oi.size ASC
#     ) AS inventory_details
# FROM
#     ordered_inventory AS oi
# JOIN
#     product_product AS prd
# ON
#     oi.product_id = prd.id
# JOIN
#     product_category AS pcat
# ON
#     prd.category_id = pcat.id
# JOIN
#     product_color AS pcol
# ON
#     prd.color_id = pcol.id
# WHERE
# 	prd.category_id = 1
# 		AND
# 	prd.color_id = 1
# GROUP BY
#     prd.id,
#     pcat.title,
#     pcol.title
# ORDER BY
#     prd.id;


from django.db import (
    models,
)
from django.db.models import F, Case, When, Value, BooleanField, Sum, Min, Max

from django.db.models import (
    F,
    Case,
    When,
    Value,
    CharField,
    Subquery,
    OuterRef,
    ExpressionWrapper,
)
from django.db.models.functions import Concat, ConcatPair
from django.contrib.postgres.aggregates import StringAgg, JSONBAgg
from django.db.models.expressions import RawSQL

from design_patterns_crafted_django_e_commerce.product.models import Category, Product
from django.db import connection

from django.db.models.functions import JSONObject


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
                # inventory_details=StringAgg(
                #     Concat(
                #         Value("inventory_id:"),
                #         "id",
                #         Value(";size:"),
                #         "size",
                #         Value(";price:"),
                #         "price",
                #         Value(";stock_status:"),
                #         Case(
                #             When(quantity=0, then=Value("Sold Out")),
                #             default=Value("In Stock"),
                #             output_field=CharField(),
                #         ),
                #         output_field=CharField(),
                #     ),
                #     delimiter="|",
                # )
            )
        )

        # with connection.cursor() as cursor:
        # # Your raw SQL query here
        #     query = """
        #     WITH ordered_inventory AS (
        #         SELECT
        #             inv.id AS inventory_id,
        #             inv.size,
        #             inv.price,
        #             inv.quantity,
        #             inv.product_id
        #         FROM
        #             inventory_inventory AS inv
        #         ORDER BY
        #             inv.product_id, inv.size ASC
        #     )
        #     SELECT
        #         prd.first_image_url,
        #         prd.second_image_url,
        #         prd.description,
        #         pcat.title AS category,
        #         pcol.title AS color,
        #         STRING_AGG(
        #             CONCAT_WS(
        #                 ';',
        #                 CONCAT('inventory_id', ':', oi.inventory_id),
        #                 CONCAT('size', ':', oi.size),
        #                 CONCAT('price', ':', oi.price),
        #                 CASE
        #                     WHEN oi.quantity = 0 THEN 'Sold Out'
        #                     ELSE 'In Stock'
        #                 END
        #             ), ', '
        #             ORDER BY oi.size ASC
        #         ) AS inventory_details
        #     FROM
        #         ordered_inventory AS oi
        #     JOIN
        #         product_product AS prd
        #     ON
        #         oi.product_id = prd.id
        #     JOIN
        #         product_category AS pcat
        #     ON
        #         prd.category_id = pcat.id
        #     JOIN
        #         product_color AS pcol
        #     ON
        #         prd.color_id = pcol.id
        #     WHERE
        #         prd.category_id = %s
        #         AND
        #         prd.color_id = %s
        #     GROUP BY
        #         prd.id,
        #         pcat.title,
        #         pcol.title
        #     ORDER BY
        #         prd.id;
        #     """

        #     cursor.execute(query, [category_pk, color_pk])
        #     # Fetch the results
        #     result = cursor.fetchall()

        return result

    def get_product_into_product_page(self):
        pass
