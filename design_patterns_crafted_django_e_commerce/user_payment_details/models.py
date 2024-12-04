from datetime import datetime

from django.core.exceptions import (
    ValidationError,
)

from django.db import (
    models,
)

from design_patterns_crafted_django_e_commerce.common.models import (
    BaseUserCharField,
)

from .constants import (
    CARD_HOLDER_RULES,
    CARD_NUMBER_RULES,
    CVV_CODE_RULES,
)


class MonthChoices(models.TextChoices):
    @classmethod
    def generate_choices(cls):
        return [(f"{month:02}", f"{month:02}") for month in range(1, 13)]


class YearChoices(models.TextChoices):
    @classmethod
    def generate_choices(cls):
        current_year = datetime.now().year
        return [
            (str(year), str(year)) for year in range(current_year, current_year + 12)
        ]


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

    expiry_month = models.CharField(
        max_length=2,
        choices=MonthChoices.generate_choices(),
    )

    expiry_year = models.CharField(
        max_length=4,
        choices=YearChoices.generate_choices(),
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
        if not self.expiry_month or not self.expiry_year:
            return
        
        current_date = datetime.now()
        current_month = current_date.month
        current_year = current_date.year

        expiry_month = int(self.expiry_month)
        expiry_year = int(self.expiry_year)

        if expiry_year < current_year:
            raise ValidationError("This card has expired")

        if expiry_year == current_year and expiry_month < current_month:
            raise ValidationError("This card has expired")

    def save(self, *args, **kwargs):

        self.clean()

        super().save(*args, **kwargs)
