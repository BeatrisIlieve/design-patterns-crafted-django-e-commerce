"""
1. Set up a PostgreSQL database
2. Run python manage.py makemigrations
3. Run python manage.py migrate
4. Run python manage.py initialize_products_data
5. Run python manage.py initialize_inventory_data
6. Run the current file
7. Compare the result with the output at the bottom of the current file
"""

import os
import django


os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "design_patterns_crafted_django_e_commerce.settings"
)
django.setup()

from django.core.exceptions import (
    ValidationError,
)
from django.db.utils import (
    IntegrityError,
)

from design_patterns_crafted_django_e_commerce.user_credential_details.models import (
    UserCredentialDetails,
)
from design_patterns_crafted_django_e_commerce.product.strategies.filtration import (
    FiltrationMethod,
    execute_filtration,
)
from design_patterns_crafted_django_e_commerce.product.models import (
    Category,
    Color,
    Product,
)
from design_patterns_crafted_django_e_commerce.product.strategies.product_set import (
    ProductSetMethod,
    execute_product_set,
)
from design_patterns_crafted_django_e_commerce.wishlist.models import (Wishlist,)


def test_register_user(email: str, password: str) -> str:
    try:
        UserCredentialDetails.objects.create(email=email, password=password)
        return f"User with email {email} has successfully registered."
    except ValidationError as e:
        return e.messages[0]


def test_register_user_with_duplicate_email(email: str, password: str) -> str:
    try:
        UserCredentialDetails.objects.create(email=email, password=password)
        return f"User with email {email} has successfully registered."
    except ValidationError as e:
        return e.messages[0]


def test_get_product_details_into_product_list_page(category_pk, color_pk):

    return execute_filtration(
        category_pk, color_pk, FiltrationMethod.INTO_PRODUCTS_LIST
    )
    

def test_get_product_details_into_product_page(category_pk, color_pk):

    return execute_filtration(category_pk, color_pk, FiltrationMethod.INTO_PRODUCT_PAGE)


def test_get_pink_product_set(method: ProductSetMethod) -> str:
    return execute_product_set(method)

def test_execute_clicking_on_the_like_button_expect_to_add(product, user):
    return Wishlist.objects.execute_like_button_click(product, user)

def test_get_products_in_user_wishlist(user):
    return Wishlist.objects.get_all_liked_products(user)

def test_execute_clicking_on_the_like_button_expect_to_remove(product, user):
    return Wishlist.objects.execute_like_button_click(product, user)
        


print(test_register_user(email="beatrisilieve@icloud.com", password="123456Aa@"))
print()
print(
    test_register_user_with_duplicate_email(
        email="beatrisilieve@icloud.com", password="123456Aa@"
    )
)
print()
category_pk_1 = Category.objects.get(title="E").pk
color_pk_1 = Color.objects.get(title="P").pk

# print(test_get_product_details_into_product_list_page(category_pk_1, color_pk_1))
print()
# print(test_get_product_details_into_product_page(category_pk_1, color_pk_1))
print()
# print(test_get_pink_product_set(ProductSetMethod.PINK_SET))
print()
product = Product.objects.filter(category_id=category_pk_1, color_id=color_pk_1).first()
user = UserCredentialDetails.objects.get(email="beatrisilieve@icloud.com")
print(test_execute_clicking_on_the_like_button_expect_to_add(product, user))
print()
print(test_get_products_in_user_wishlist(user))
print()
print(test_execute_clicking_on_the_like_button_expect_to_remove(product, user))
"""
OUTPUT:

User with email beatrisilieve@icloud.com has successfully registered. 

User with that email address already exists.

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

Category: Earrings
Color: Pink
First Image: https://res.cloudinary.com/deztgvefu/image/upload/v1723714885/forget-me-not-collection/earrings/forget_me_not_drop_earrings_diamond_and_pink_sapphire_eapspdrflrfmn_ee-1_zzaw4q.webp
Second Image: https://res.cloudinary.com/deztgvefu/image/upload/v1723714886/forget-me-not-collection/earrings/forget_me_not_drop_earrings_diamond_and_pink_sapphire_eapspdrflrfmn_ee-2_p9jicb.webp
Price Range: 43000.00 - 45000.00
Is sold out: False

Product has been added to wishlist

Category: Earrings
Color: Pink
First Image: https://res.cloudinary.com/deztgvefu/image/upload/v1723714885/forget-me-not-collection/earrings/forget_me_not_drop_earrings_diamond_and_pink_sapphire_eapspdrflrfmn_ee-1_zzaw4q.webp
Second Image: https://res.cloudinary.com/deztgvefu/image/upload/v1723714886/forget-me-not-collection/earrings/forget_me_not_drop_earrings_diamond_and_pink_sapphire_eapspdrflrfmn_ee-2_p9jicb.webp
Price Range: 43000.00 - 45000.00
Is sold out: False

Product has been added to wishlist

Category: Earrings
Color: Pink
First Image: https://res.cloudinary.com/deztgvefu/image/upload/v1723714885/forget-me-not-collection/earrings/forget_me_not_drop_earrings_diamond_and_pink_sapphire_eapspdrflrfmn_ee-1_zzaw4q.webp
Second Image: https://res.cloudinary.com/deztgvefu/image/upload/v1723714886/forget-me-not-collection/earrings/forget_me_not_drop_earrings_diamond_and_pink_sapphire_eapspdrflrfmn_ee-2_p9jicb.webp
Price Range: 43000.00 - 45000.00
Is sold out: False

Product has removed from the wishlist
"""
