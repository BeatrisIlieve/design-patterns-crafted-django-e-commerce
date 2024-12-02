"""
1. Set up a PostgreSQL database
2. Run python manage.py makemigrations
3. Run python manage.py migrate
4. Run python manage.py initialize_products_data
5. Run python manage.py initialize_inventory_data
6. Run the current file
7. Compare the result with the output at the bottom of the current file
"""

import json
import os
import django


os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "design_patterns_crafted_django_e_commerce.settings"
)
django.setup()

from django.core.exceptions import (
    ValidationError,
)

from design_patterns_crafted_django_e_commerce.user_credential_details.models import (
    UserCredentialDetails,
)

from design_patterns_crafted_django_e_commerce.product.models import (
    Category,
    Color,
    Product,
)

from design_patterns_crafted_django_e_commerce.wishlist.models import (
    Wishlist,
)
from design_patterns_crafted_django_e_commerce.shopping_bag.models import (
    ShoppingBag,
)
from design_patterns_crafted_django_e_commerce.inventory.models import (
    Inventory,
)


class TestEntireFunctionality:
    def __init__(self) -> None:
        self.__user_email: str = "beatrisilieve@icloud.com"
        self.__user_password: str = "123456Aa@"
        self.__category_pk_1: int = Category.objects.get(title="E").pk
        self.__color_pk_1: int = Color.objects.get(title="P").pk
        self.__product: Product = Product.objects.filter(
            category_id=self.__category_pk_1, color_id=self.__color_pk_1
        ).first()
        self.__user: UserCredentialDetails = None

    def __test_register_user(self) -> str:
        try:
            user = UserCredentialDetails.objects.create(
                email=self.__user_email, password=self.__user_password
            )

            self.__user = user

            return f"User with email {self.__user_email} has successfully registered."
        except ValidationError as e:
            return e.messages[0]

    def __test_register_user_with_duplicate_email(self) -> str:
        try:
            UserCredentialDetails.objects.create(
                email=self.__user_email, password=self.__user_password
            )
            return f"User with email {self.__user_email} has successfully registered."
        except ValidationError as e:
            return e.messages[0]

    def __test_get_product_into_product_page(self) -> str:

        inventories = Inventory.objects.get_product_into_product_page(
            self.__category_pk_1, self.__color_pk_1
        )

        inventory_details = inventories[0]["inventory_details"]

        sizes_by_inventory_id_and_price = []

        for item in inventory_details:
            for key, value in item.items():
                sizes_by_inventory_id_and_price.append(f"{key}: {value}")
            sizes_by_inventory_id_and_price.append("\n")

        result = "\n\n".join(
            [
                "Product details into products list page:",
                f"First image: {inventories[0]['product__first_image_url']}",
                f"Second image: {inventories[0]['product__second_image_url']}",
                f"Description: {inventories[0]['product__description']}",
                f"Category: {inventories[0]['full_category_title']}",
                f"Color: {inventories[0]['full_color_title']}",
                "\n".join(sizes_by_inventory_id_and_price),
            ]
        )

        return result

    def __test_get_product_into_products_list_page(self):
        inventories = Inventory.objects.get_product_into_products_list(
            self.__category_pk_1, self.__color_pk_1
        )
        
        return inventories

    def __test_execute_clicking_on_the_like_button_expect_to_add(self):
        return Wishlist.objects.execute_like_button_click(self.__product, self.__user)

    def __test_get_products_in_user_wishlist(self):
        return Wishlist.objects.get_all_liked_products(self.__user)

    def __test_execute_clicking_on_the_like_button_expect_to_remove(self):
        return Wishlist.objects.execute_like_button_click(self.__product, self.__user)

    def __test_execute_clicking_on_the_add_to_bag_button(self):
        return Inventory.get_product_into_products_list(
            self.__category_pk_1, self.__color_pk_1
        )

    def execute(self):
        # result = self.__test_get_product_into_product_page()
        
        result = self.__test_get_product_into_products_list_page()

        # result.append(self.__test_register_user())
        # result.append(self.__test_register_user_with_duplicate_email())
        # result.append(self.__test_execute_clicking_on_the_like_button_expect_to_add())
        # result.append(self.__test_get_products_in_user_wishlist())
        # result.append(
        #     self.__test_execute_clicking_on_the_like_button_expect_to_remove()
        # )
        # result.append(self.__test_get_product_into_product_page())
        return result
        # return "\n\n".join(result)


instance = TestEntireFunctionality()

print(instance.execute())

# OUTPUT:
"""
User with email beatrisilieve@icloud.com has successfully registered. 

User with that email address already exists

Category: Earrings
Color: Pink
First Image: https://res.cloudinary.com/deztgvefu/image/upload/v1723714885/forget-me-not-collection/earrings/forget_me_not_drop_earrings_diamond_and_pink_sapphire_eapspdrflrfmn_ee-1_zzaw4q.webp
Second Image: https://res.cloudinary.com/deztgvefu/image/upload/v1723714886/forget-me-not-collection/earrings/forget_me_not_drop_earrings_diamond_and_pink_sapphire_eapspdrflrfmn_ee-2_p9jicb.webp
Price Range: 43000.00 - 45000.00
Is sold out: False

Category: Earrings
Color: Pink
First Image: https://res.cloudinary.com/deztgvefu/image/upload/v1723714885/forget-me-not-collection/earrings/forget_me_not_drop_earrings_diamond_and_pink_sapphire_eapspdrflrfmn_ee-1_zzaw4q.webp
Second Image: https://res.cloudinary.com/deztgvefu/image/upload/v1723714886/forget-me-not-collection/earrings/forget_me_not_drop_earrings_diamond_and_pink_sapphire_eapspdrflrfmn_ee-2_p9jicb.webp
Description: 28 pear-shaped and round brilliant sapphires weighing a total of approximately 3.20 carats and 28 marquise and round brilliant diamonds weighing a total of approximately 1.98 carats, set in platinum.
Size Measurement: 4.05
Inventory Quantity: 3
Price Amount: 43000.00
Is Sold Out: No
Size Measurement: 4.98
Inventory Quantity: 3
Price Amount: 44000.00
Is Sold Out: No
Size Measurement: 5.86
Inventory Quantity: 3
Price Amount: 45000.00
Is Sold Out: No

Category: Earrings
Color: Pink
First Image: https://res.cloudinary.com/deztgvefu/image/upload/v1723714885/forget-me-not-collection/earrings/forget_me_not_drop_earrings_diamond_and_pink_sapphire_eapspdrflrfmn_ee-1_zzaw4q.webp
Second Image: https://res.cloudinary.com/deztgvefu/image/upload/v1723714886/forget-me-not-collection/earrings/forget_me_not_drop_earrings_diamond_and_pink_sapphire_eapspdrflrfmn_ee-2_p9jicb.webp
Price Range: 43000.00 - 45000.00
Is sold out: False
Category: Bracelets
Color: Pink
First Image: https://res.cloudinary.com/deztgvefu/image/upload/v1723714894/forget-me-not-collection/bracelets/forget_me_not_bracelet_diamond_and_pink_sapphire_brpsprfflrfmn_e_1_vz9pv4.avif
Second Image: https://res.cloudinary.com/deztgvefu/image/upload/v1723714893/forget-me-not-collection/bracelets/forget_me_not_bracelet_diamond_and_pink_sapphire_brpsprfflrfmn_e_2_kdpnm6.avif
Price Range: 34000.00 - 36000.00
Is sold out: False
Category: Necklaces
Color: Pink
First Image: https://res.cloudinary.com/deztgvefu/image/upload/v1723714890/forget-me-not-collection/necklaces/forget_me_not_lariat_necklace_diamond_and_pink_sapphire_nkpspltflrfmn_e_1_kuxbds.webp
Second Image: https://res.cloudinary.com/deztgvefu/image/upload/v1723714890/forget-me-not-collection/necklaces/forget_me_not_lariat_necklace_diamond_and_pink_sapphire_nkpspltflrfmn_e_2_d2fc78.webp
Price Range: 55000.00 - 57000.00
Is sold out: False
Category: Rings
Color: Pink
First Image: https://res.cloudinary.com/deztgvefu/image/upload/v1723714892/forget-me-not-collection/rings/forget_me_not_ring_diamond_and_pink_sapphire_frpsprfflrfmn_e_1_qfumu3.webp
Second Image: https://res.cloudinary.com/deztgvefu/image/upload/v1723714892/forget-me-not-collection/rings/forget_me_not_ring_diamond_and_pink_sapphire_frpsprfflrfmn_e_2_k7nhpe.avif
Price Range: 23000.00 - 25000.00
Is sold out: False

Product has been added to wishlist

Category: Earrings
Color: Pink
First Image: https://res.cloudinary.com/deztgvefu/image/upload/v1723714885/forget-me-not-collection/earrings/forget_me_not_drop_earrings_diamond_and_pink_sapphire_eapspdrflrfmn_ee-1_zzaw4q.webp
Second Image: https://res.cloudinary.com/deztgvefu/image/upload/v1723714886/forget-me-not-collection/earrings/forget_me_not_drop_earrings_diamond_and_pink_sapphire_eapspdrflrfmn_ee-2_p9jicb.webp
Price Range: 43000.00 - 45000.00
Is sold out: False

Product has been removed from the wishlist
"""
