from django.db import (
    models,
)

from design_patterns_crafted_django_e_commerce.product.strategies.filtration import (
    FiltrationMethod,
    execute_filtration,
)


class WishlistManager(models.Manager):
    def get_all_liked_products(self, user) -> str:
        wishlist_items = self.filter(user=user).select_related("product", "product__category", "product__color")
        result = []

        for wishlist_item in wishlist_items:
            product = wishlist_item.product
            category_pk = product.category.id
            color_pk = product.color.id

            product_details = execute_filtration(
                category_pk, color_pk, FiltrationMethod.INTO_PRODUCTS_LIST
            )

            result.append(product_details)

        return "\n".join(result)


    def check_if_a_product_is_liked_by_user(self, product, user):
        pass
