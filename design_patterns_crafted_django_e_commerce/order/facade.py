from django.core.exceptions import (
    ValidationError,
)
from django.db.models.functions import (
    TruncDate,
)
from django.db.models import (
    F,
    Case,
    Value,
    When,
    CharField,
)
from design_patterns_crafted_django_e_commerce.user_payment_details.models import (
    UserPaymentDetails,
)
from design_patterns_crafted_django_e_commerce.shopping_bag.models import (
    ShoppingBag,
)
from design_patterns_crafted_django_e_commerce.order.models import (
    Order,
    OrderItem,
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


class MoveShoppingBagItemsToOrderItem:
    def move_items(self, user_pk):
        bag_items = ShoppingBag.objects.filter(user=user_pk)

        order = Order.objects.get(user=user_pk)

        for bag_item in bag_items:
            inventory = bag_item.inventory
            quantity = bag_item.quantity

            OrderItem.objects.create(
                order=order, inventory=inventory, quantity=quantity
            )

            bag_item.delete()

        return order


class GenerateOrderConfirmation:
    def generate(self, user_pk):
        return (
            Order.objects.filter(user_id=user_pk)
            .select_related("delivery")
            .prefetch_related("order_item_order__inventory__product")
            .annotate(
                created_date=TruncDate("created_at"),
                total_price_per_product=F("order_item_order__inventory__price")
                * F("order_item_order__quantity"),
                delivery_method_full_title=Case(
                    When(delivery__method="SP", then=Value("Store Pickup")),
                    When(delivery__method="EH", then=Value("Express Home")),
                    When(delivery__method="RH", then=Value("Regular Home")),
                    default=Value("Unknown Method"),
                    output_field=CharField(),
                ),
            )
            .values(
                "created_date",
                "order_item_order__quantity",
                "order_item_order__inventory__price",
                "total_price_per_product",
                "order_item_order__inventory__size",
                "order_item_order__inventory__product__first_image_url",
                "delivery_method_full_title",
                "delivery__total_cost",
                "delivery__due_date",
            )
            .order_by("order_item_order__pk")
        )


class OrderFacade:
    def __init__(
        self,
        update_user_payment_details: UpdateUserPaymentDetails,
        move_shopping_bag_items_to_order_item: MoveShoppingBagItemsToOrderItem,
        generate_order_confirmation: GenerateOrderConfirmation,
    ):
        self.update_user_payment_details: UpdateUserPaymentDetails = (
            update_user_payment_details
        )
        self.move_shopping_bag_items_to_order_item: MoveShoppingBagItemsToOrderItem = (
            move_shopping_bag_items_to_order_item
        )

        self.generate_order_confirmation: GenerateOrderConfirmation = (
            generate_order_confirmation
        )

    def operation(self, user_pk, payment_details):

        self.update_user_payment_details.update_related_obj(user_pk, payment_details)

        self.move_shopping_bag_items_to_order_item.move_items(user_pk)

        return self.generate_order_confirmation.generate(user_pk)


def client_code_order(facade: OrderFacade, user_pk, payment_details):
    return facade.operation(user_pk, payment_details)
