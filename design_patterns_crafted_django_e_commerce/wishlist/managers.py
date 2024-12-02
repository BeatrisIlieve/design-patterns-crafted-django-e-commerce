from django.db import (
    models,
)

from design_patterns_crafted_django_e_commerce.inventory.models import (
    Inventory,
)
from design_patterns_crafted_django_e_commerce.product.models import (
    Product,
)


class WishlistManager(models.Manager):
    def get_all_liked_products(self, user) -> str:
        wishlist_items = self.filter(user=user).select_related(
            "product", "product__category_set", "product__color_set"
        )
        result = []

        for wishlist_item in wishlist_items:
            product = wishlist_item.product
            category_pk = product.category.id
            color_pk = product.color.id

            product_details = Inventory.objects.get_product_into_products_list(
                category_pk,
                color_pk,
            )

            result.append(product_details)

        return "\n".join(result)

    def check_if_a_product_is_liked_by_user(self, product, user):
        return self.filter(user=user, product=product).exists()

    def add_product_to_wishlist(self, product_pk, user):
        product = Product.objects.get(pk=product_pk)
        self.create(product=product, user=user)

        return "Product has been added to wishlist"

    def remove_product_from_wishlist(self, product_pk, user):
        product = Product.objects.get(pk=product_pk)
        self.filter(product=product, user=user).delete()

        return "Product has been removed from the wishlist"
