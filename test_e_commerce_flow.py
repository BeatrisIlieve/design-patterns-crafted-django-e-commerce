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


print(test_register_user(email="beatrisilieve@icloud.com", password="123456Aa@"))

print(
    test_register_user_with_duplicate_email(
        email="beatrisilieve@icloud.com", password="123456Aa@"
    )
)

# run python manage.py initialize_products_data


def test_get_product_details_into_product_list_page(category_pk, color_pk):

    return execute_filtration(
        category_pk, color_pk, FiltrationMethod.INTO_PRODUCTS_LIST
    )


"""
OUTPUT:

User with email beatrisilieve@icloud.com has successfully registered. 
User with that email address already exists.
"""
