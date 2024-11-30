from abc import (
    ABC,
    abstractmethod,
)
from enum import (
    Enum,
)

from design_patterns_crafted_django_e_commerce.product.factories.product_set import (
    PinkProductSetFactory,
    BlueProductSetFactory,
    WhiteProductSetFactory,
)


class ProductSetMethod(Enum):
    PINK_SET = "pink_set"
    BLUE_SET = "blue_set"
    WHITE_SET = "white_set"


class ProductSetStrategy(ABC):
    @abstractmethod
    def get_product_set(color_pk):
        pass


class PinkProductSet(ProductSetStrategy):
    def get_product_set(self):
        factory = PinkProductSetFactory()
        return factory.generate_product_set()


class BlueProductSet(ProductSetStrategy):
    def get_product_set(self):
        return BlueProductSetFactory()


class WhiteProductSet(ProductSetStrategy):
    def get_product_set(self):
        return WhiteProductSetFactory()


class ProductSetContext:
    def __init__(self, strategy: ProductSetStrategy):
        self._strategy = strategy

    @property
    def strategy(self) -> ProductSetStrategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: ProductSetStrategy) -> None:

        self._strategy = strategy

    def get_product_set(self):
        return self._strategy.get_product_set()


def execute_product_set(method: ProductSetMethod):

    strategies = {
        ProductSetMethod.PINK_SET: PinkProductSet(),
        ProductSetMethod.BLUE_SET: BlueProductSet(),
        ProductSetMethod.WHITE_SET: WhiteProductSet(),
    }

    context = ProductSetContext(strategy=strategies[method])
    return context.get_product_set()
