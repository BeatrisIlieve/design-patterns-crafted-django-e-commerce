from django.core.exceptions import (
    ValidationError,
)

from design_patterns_crafted_django_e_commerce.user_shipping_details.models import (
    UserShippingDetails,
)


class UpdateUserShippingDetails:
    def update_related_obj(self, user_pk, shipping_details):
        obj = UserShippingDetails.objects.get(user_id=user_pk)

        obj.first_name = shipping_details["first_name"]
        obj.last_name = shipping_details["last_name"]
        obj.phone_number = shipping_details["phone_number"]
        obj.country = shipping_details["country"]
        obj.city = shipping_details["city"]
        obj.region = shipping_details["region"]
        obj.street_address = shipping_details["street_address"]
        obj.apartment = shipping_details["apartment"]
        obj.postal_code = shipping_details["postal_code"]

        return self.__save_user_details(obj)

    def __save_user_details(self, obj):
        try:
            obj.full_clean()
            obj.save()

            return "User Shipping Details has been save successfully"

        except ValidationError as e:
            return e.messages


class Facade:
    def __init__(
        self,
        update_user_shipping_details: UpdateUserShippingDetails,
    ) -> None:
        self._update_user_shipping_details: UpdateUserShippingDetails = (
            update_user_shipping_details
        )

    def operation(self, user_pk, shipping_details):
        result = []

        result.append(
            self._update_user_shipping_details.update_related_obj(
                user_pk, shipping_details
            )
        )

        return "\n".join(result)


def client_code(facade: Facade, user_pk, method, shipping_details):
    return facade.operation(user_pk, method, shipping_details)
