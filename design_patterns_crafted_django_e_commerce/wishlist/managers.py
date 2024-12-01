from django.db import (
    models,
)


class WishlistManager(models.Manager):
    # def get_all_liked_products(self, user) -> str:
    #     wishlist_items = self.filter(user=user).select_related(
    #         "product", "product__category_set", "product__color_set"
    #     )
    #     result = []

    #     for wishlist_item in wishlist_items:
    #         product = wishlist_item.product
    #         category_pk = product.category.id
    #         color_pk = product.color.id

    #         product_details = execute_filtration(
    #             category_pk, color_pk, FiltrationMethod.INTO_PRODUCTS_LIST
    #         )

    #         result.append(product_details)

    #     return "\n".join(result)

    def __check_if_a_product_is_liked_by_user(self, product, user):
        return self.filter(user=user, product=product).exists()

    def __add_product_to_wishlist(self, product, user):
        self.create(product=product, user=user)

        return "Product has been added to wishlist"

    def __remove_product_from_wishlist(self, product, user):
        self.filter(product=product, user=user).delete()

        return "Product has been removed from the wishlist"

    def execute_like_button_click(self, product, user):
        if self.__check_if_a_product_is_liked_by_user(product, user):
            return self.__remove_product_from_wishlist(product, user)

        return self.__add_product_to_wishlist(product, user)
