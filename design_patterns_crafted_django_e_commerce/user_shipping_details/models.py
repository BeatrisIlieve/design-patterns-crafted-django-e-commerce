from django.db import (
    models,
)

from cities_light.models import (
    City,
    Country,
    Region,
)

from design_patterns_crafted_django_e_commerce.common.models import (
    BaseUserCharField,
)

from .constants import (
    FIRST_NAME_RULES,
    LAST_NAME_RULES,
    PHONE_NUMBER_RULES,
    STREET_ADDRESS_RULES,
    APARTMENT_RULES,
    POSTAL_CODE_RULES,
)


class UserShippingDetails(BaseUserCharField):

    first_name = BaseUserCharField.create_char_field(
        max_length=FIRST_NAME_RULES["max_length"],
        min_length=FIRST_NAME_RULES["min_length"],
        pattern=FIRST_NAME_RULES["pattern"],
        pattern_error_message=FIRST_NAME_RULES["pattern_error_message"],
        null_value=FIRST_NAME_RULES["null"],
        blank_value=FIRST_NAME_RULES["blank"],
    )

    last_name = BaseUserCharField.create_char_field(
        max_length=LAST_NAME_RULES["max_length"],
        min_length=LAST_NAME_RULES["min_length"],
        pattern=LAST_NAME_RULES["pattern"],
        pattern_error_message=LAST_NAME_RULES["pattern_error_message"],
        null_value=LAST_NAME_RULES["null"],
        blank_value=LAST_NAME_RULES["blank"],
    )

    phone_number = BaseUserCharField.create_char_field(
        max_length=PHONE_NUMBER_RULES["max_length"],
        min_length=PHONE_NUMBER_RULES["min_length"],
        pattern=PHONE_NUMBER_RULES["pattern"],
        pattern_error_message=PHONE_NUMBER_RULES["pattern_error_message"],
        null_value=PHONE_NUMBER_RULES["null"],
        blank_value=PHONE_NUMBER_RULES["blank"],
    )

    country = models.ForeignKey(
        to=Country,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
    )

    city = models.ForeignKey(
        to=City,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
    )

    region = models.ForeignKey(
        to=Region,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
    )

    street_address = BaseUserCharField.create_char_field(
        max_length=STREET_ADDRESS_RULES["max_length"],
        min_length=STREET_ADDRESS_RULES["min_length"],
        pattern=STREET_ADDRESS_RULES["pattern"],
        pattern_error_message=STREET_ADDRESS_RULES["pattern_error_message"],
        null_value=STREET_ADDRESS_RULES["null"],
        blank_value=STREET_ADDRESS_RULES["blank"],
    )

    apartment = BaseUserCharField.create_char_field(
        max_length=APARTMENT_RULES["max_length"],
        min_length=APARTMENT_RULES["min_length"],
        pattern=APARTMENT_RULES["pattern"],
        pattern_error_message=APARTMENT_RULES["pattern_error_message"],
        null_value=APARTMENT_RULES["null"],
        blank_value=APARTMENT_RULES["blank"],
    )

    postal_code = BaseUserCharField.create_char_field(
        max_length=POSTAL_CODE_RULES["max_length"],
        min_length=POSTAL_CODE_RULES["min_length"],
        pattern=POSTAL_CODE_RULES["pattern"],
        pattern_error_message=POSTAL_CODE_RULES["pattern_error_message"],
        null_value=POSTAL_CODE_RULES["null"],
        blank_value=POSTAL_CODE_RULES["blank"],
    )

    user = models.OneToOneField(
        to="user_credential_details.UserCredentialDetails",
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="shipping_details",
    )
