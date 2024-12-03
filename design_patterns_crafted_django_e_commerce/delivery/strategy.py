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
    STORE_PICKUP = "Store Pickup"
    EXPRESS_HOME = "Express Home Delivery"
    REGULAR_HOME = "Regular Home Delivery"


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


class DeliveryContext:
    def __init__(self, strategy: DeliveryStrategy) -> None:
        self.strategy = strategy

    def get_delivery_details(self, user_pk):
        method = self.strategy.get_method_choice_name()
        total_cost = self.strategy.calculate_total_order_cost(user_pk)
        due_date = self.strategy.calculate_delivery_due_date()

        return {"method": method, "total_cost": total_cost, "due_date": due_date}


def execute_context(user_pk, method):
    strategies = {
        DeliveryMethod.STORE_PICKUP: StorePickupStrategy(),
        DeliveryMethod.EXPRESS_HOME: ExpressHomeDeliveryStrategy(),
        DeliveryMethod.REGULAR_HOME: RegularHomeDeliveryStrategy(),
    }

    context = DeliveryContext(strategy=strategies[method])
    return context.get_delivery_details(user_pk)
