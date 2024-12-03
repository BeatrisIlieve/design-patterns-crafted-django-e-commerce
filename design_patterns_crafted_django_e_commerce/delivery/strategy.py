from enum import (
    Enum,
)
from abc import (
    ABC,
    abstractmethod,
)
from decimal import (
    Decimal,
)
from datetime import (
    timedelta,
)
from django.utils.timezone import (
    now,
)

from design_patterns_crafted_django_e_commerce.shopping_bag.models import ShoppingBag
from design_patterns_crafted_django_e_commerce.user_credential_details.models import (
    UserCredentialDetails,
)


class DeliveryMethod(Enum):
    SP = "Store Pickup"
    EH = "Express Home Delivery"
    RH = "Regular Home Delivery"


class DeliveryStrategy(ABC):
    @abstractmethod
    def get_method_choice_name(self) -> str:
        pass

    @abstractmethod
    def calculate_total_order_cost(self, user) -> float:
        pass

    @abstractmethod
    def calculate_delivery_due_date(self) -> str:
        pass


class StorePickupStrategy(DeliveryStrategy):
    DELIVERY_COST = 0

    def get_method_choice_name(self) -> str:
        return "SP"

    def calculate_total_order_cost(self, user) -> float:

        shopping_bag_total_price = ShoppingBag.objects.calculate_total_price(user)

        delivery_cost = Decimal(StorePickupStrategy.DELIVERY_COST)

        total_cost = shopping_bag_total_price + delivery_cost

        return total_cost

    def calculate_delivery_due_date(self) -> str:
        return now().date()


class ExpressHomeDeliveryStrategy(DeliveryStrategy):
    DELIVERY_COST = 30

    def get_method_choice_name(self) -> str:
        return "EH"

    def calculate_total_order_cost(self, user) -> float:

        shopping_bag_total_price = ShoppingBag.objects.calculate_total_price(user)

        delivery_cost = Decimal(ExpressHomeDeliveryStrategy.DELIVERY_COST)

        total_cost = shopping_bag_total_price + delivery_cost

        return total_cost

    def calculate_delivery_due_date(self) -> str:
        return now().date() + timedelta(days=2)


class RegularHomeDeliveryStrategy(DeliveryStrategy):
    DELIVERY_COST = 10

    def get_method_choice_name(self) -> str:
        return "RH"

    def calculate_total_order_cost(self, user) -> float:

        shopping_bag_total_price = ShoppingBag.objects.calculate_total_price(user)

        delivery_cost = Decimal(ExpressHomeDeliveryStrategy.DELIVERY_COST)

        total_cost = shopping_bag_total_price + delivery_cost

        return total_cost

    def calculate_delivery_due_date(self) -> str:
        return now().date() + timedelta(days=7)
