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


"""
OUTPUT:

User with email beatrisilieve@icloud.com has successfully registered. 
User with that email address already exists.
"""
