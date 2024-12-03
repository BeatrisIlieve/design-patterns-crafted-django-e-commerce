from enum import (
    Enum,
)
from abc import (
    ABC,
    abstractmethod,
)
from datetime import (
    timedelta,
)
from django.utils.timezone import (
    now,
)

from design_patterns_crafted_django_e_commerce.utils.functions.calculate_total_delivery_cost import (
    calculate_total_delivery_cost,
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

        return calculate_total_delivery_cost(user, StorePickupStrategy.DELIVERY_COST)

    def calculate_delivery_due_date(self) -> str:
        return now().date()


class ExpressHomeDeliveryStrategy(DeliveryStrategy):
    DELIVERY_COST = 30

    def get_method_choice_name(self) -> str:
        return "EH"

    def calculate_total_order_cost(self, user) -> float:

        return calculate_total_delivery_cost(
            user, ExpressHomeDeliveryStrategy.DELIVERY_COST
        )

    def calculate_delivery_due_date(self) -> str:
        return now().date() + timedelta(days=2)


class RegularHomeDeliveryStrategy(DeliveryStrategy):
    DELIVERY_COST = 10

    def get_method_choice_name(self) -> str:
        return "RH"

    def calculate_total_order_cost(self, user) -> float:

        return calculate_total_delivery_cost(
            user, RegularHomeDeliveryStrategy.DELIVERY_COST
        )

    def calculate_delivery_due_date(self) -> str:
        return now().date() + timedelta(days=7)