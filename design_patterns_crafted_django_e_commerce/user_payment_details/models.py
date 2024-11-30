from django.db import (
    models,
)
from django.core.exceptions import (
    ValidationError,
)
from django.utils.timezone import (
    now,
)

from design_patterns_crafted_django_e_commerce.common.models import (
    BaseUserCharField,
)

from .constants import (
    CARD_HOLDER_RULES,
    CARD_NUMBER_RULES,
    CVV_CODE_RULES,
    EXPIRY_DATE_RULES,
)


class UserPaymentDetails(BaseUserCharField):

    card_holder = BaseUserCharField.create_char_field(
        max_length=CARD_HOLDER_RULES["max_length"],
        min_length=CARD_HOLDER_RULES["min_length"],
        pattern=CARD_HOLDER_RULES["pattern"],
        pattern_error_message=CARD_HOLDER_RULES["pattern_error_message"],
        null_value=CARD_HOLDER_RULES["null"],
        blank_value=CARD_HOLDER_RULES["blank"],
    )

    card_number = BaseUserCharField.create_char_field(
        max_length=CARD_NUMBER_RULES["max_length"],
        min_length=CARD_NUMBER_RULES["min_length"],
        pattern=CARD_NUMBER_RULES["pattern"],
        pattern_error_message=CARD_NUMBER_RULES["pattern_error_message"],
        null_value=CARD_NUMBER_RULES["null"],
        blank_value=CARD_NUMBER_RULES["blank"],
    )

    expiry_date = BaseUserCharField.create_char_field(
        max_length=EXPIRY_DATE_RULES["max_length"],
        min_length=EXPIRY_DATE_RULES["min_length"],
        pattern=EXPIRY_DATE_RULES["pattern"],
        pattern_error_message=EXPIRY_DATE_RULES["pattern_error_message"],
        null_value=EXPIRY_DATE_RULES["null"],
        blank_value=EXPIRY_DATE_RULES["blank"],
    )

    cvv_code = BaseUserCharField.create_char_field(
        max_length=CVV_CODE_RULES["max_length"],
        min_length=CVV_CODE_RULES["min_length"],
        pattern=CVV_CODE_RULES["pattern"],
        pattern_error_message=CVV_CODE_RULES["pattern_error_message"],
        null_value=CVV_CODE_RULES["null"],
        blank_value=CVV_CODE_RULES["blank"],
    )

    user = models.OneToOneField(
        to="user_credential_details.UserCredentialDetails",
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="payment_details",
    )

    def clean(self):
        if self.expiry_date:
            provided_month, provided_year = self.expiry_date.split("/")

            current_date = str(now().date())

            current_year, current_month, _ = current_date.split("-")

            if provided_year < current_year[-2:] or provided_month < current_month:
                raise ValidationError("This card has expired")

    def save(self, *args, **kwargs):
        self.clean()

        super().save(*args, **kwargs)
