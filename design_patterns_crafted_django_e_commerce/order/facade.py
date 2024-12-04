# 1. Make payment
# 2. Move shopping bag to order item
# 3. Clean shopping bag
from django.core.exceptions import (
    ValidationError,
)

from design_patterns_crafted_django_e_commerce.user_payment_details.models import (
    UserPaymentDetails,
)


class UpdateUserPaymentDetails:
    def update_related_obj(self, user_pk, payment_details):
        obj = UserPaymentDetails.objects.get(user_id=user_pk)

        obj.card_holder = payment_details["card_holder"]
        obj.card_number = payment_details["card_number"]
        obj.expiry_month = payment_details["expiry_month"]
        obj.expiry_year = payment_details["expiry_year"]
        obj.cvv_code = payment_details["cvv_code"]

        return self.__save_user_details(obj)

    def __save_user_details(self, obj):
        try:
            obj.full_clean()
            obj.save()

            return "User Payment Details have been successfully updated"

        except ValidationError as e:
            return e.messages
