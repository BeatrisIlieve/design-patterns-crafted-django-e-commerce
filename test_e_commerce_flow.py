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


print(test_register_user(email="beatrisilieve@icloud.com", password="123456Aa@"))

print(
    test_register_user_with_duplicate_email(
        email="beatrisilieve@icloud.com", password="123456Aa@"
    )
)

category_pk_1 = Category.objects.get(title="E").pk
color_pk_1 = Color.objects.get(title="P").pk

print(test_get_product_details_into_product_list_page(category_pk_1, color_pk_1))

"""
OUTPUT:

User with email beatrisilieve@icloud.com has successfully registered. 
User with that email address already exists.
"""
