from django.core.exceptions import (
    ValidationError,
)

from design_patterns_crafted_django_e_commerce.user_shipping_details.models import (
    UserShippingDetails,
)
from design_patterns_crafted_django_e_commerce.user_credential_details.models import (
    UserCredentialDetails,
)
from design_patterns_crafted_django_e_commerce.order.models import (
    Order,
)
from .strategy import (
    DeliveryMethod,
    execute_context,
)

from design_patterns_crafted_django_e_commerce.delivery.models import (
    Delivery,
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

            return "User Shipping Details have been successfully updated"

        except ValidationError as e:
            return e.messages


class CreateUserOrder:
    def create_order(self, user_pk):
        user = UserCredentialDetails.objects.get(pk=user_pk)

        order = Order.objects.create(user=user)

        return order, user


class CreateUserDelivery:
    def create_delivery(self, user: UserCredentialDetails, order: Order, method_choice):
        method_mapper = {
            "SP": DeliveryMethod.STORE_PICKUP,
            "EH": DeliveryMethod.EXPRESS_HOME,
            "RH": DeliveryMethod.REGULAR_HOME,
        }

        method = method_mapper[method_choice]

        delivery_details = execute_context(user, method)

        Delivery.objects.create(
            method=delivery_details["method"],
            total_cost=delivery_details["total_cost"],
            due_date=delivery_details["due_date"],
            order=order,
        )


class Facade:
    def __init__(
        self,
        update_user_shipping_details: UpdateUserShippingDetails,
        create_user_order: CreateUserOrder,
        create_user_delivery: CreateUserDelivery,
    ) -> None:
        self._update_user_shipping_details: UpdateUserShippingDetails = (
            update_user_shipping_details
        )
        self.create_user_order: CreateUserOrder = create_user_order
        self._order: Order = None
        self._user: UserCredentialDetails = None
        self.create_user_delivery: CreateUserDelivery = create_user_delivery

    def operation(self, user_pk, method_choice, shipping_details):
        result = []

        result.append(
            self._update_user_shipping_details.update_related_obj(
                user_pk, shipping_details
            )
        )

        self._order, self._user = self.create_user_order.create_order(user_pk)

        self.create_user_delivery.create_delivery(
            self._user, self._order, method_choice
        )

        return "\n".join(result)


def client_code(facade: Facade, user_pk, method_choice, shipping_details):
    return facade.operation(user_pk, method_choice, shipping_details)
