from abc import ABC, abstractmethod


from django_ecommerce_strategy_pattern.product.filtration_strategy import (
    get_entity_details,
    FiltrationMethod,
)

from .models import (
    Color,
    Category,
)


class AbstractProductSetFactory(ABC):
    """
    The Abstract Factory interface declares a set of methods that return
    different abstract products. These products are called a family and are
    related by a high-level theme or concept. A family of products may have
    several variants, but the products of one variant are incompatible with
    products of another.

    In this case, the products are jewelry items (earrings, bracelets,
    necklaces, and rings) of different colors (variants).
    """

    @abstractmethod
    def create_earring(self):
        pass

    @abstractmethod
    def create_bracelet(self):
        pass

    @abstractmethod
    def create_necklace(self):
        pass

    @abstractmethod
    def create_ring(self):
        pass

    @abstractmethod
    def generate_product_set(self):
        pass


class ProductMixin:
    """
    The ProductMixin class provides common functionality for creating jewelry
    items of specific categories (earrings, bracelets, necklaces, rings)
    with a specific color. It holds the logic to retrieve a product from
    the system using category and color information.
    """

    def __init__(self, color_pk: int, category_title: str) -> None:
        self.color_pk = color_pk
        self.category_pk = Category.objects.get(title=category_title).pk

    def get_product(self):
        return get_entity_details(
            self.category_pk, self.color_pk, FiltrationMethod.INTO_PRODUCTS_LIST
        )


"""
Concrete Products are created by corresponding Concrete Factories.
"""


class Earring(ProductMixin):
    CATEGORY_TITLE = "E"

    def __init__(self, color_pk: str) -> None:
        super().__init__(color_pk, Earring.CATEGORY_TITLE)


class Bracelet(ProductMixin):
    CATEGORY_TITLE = "B"

    def __init__(self, color_pk: str) -> None:
        super().__init__(color_pk, Bracelet.CATEGORY_TITLE)


class Necklace(ProductMixin):
    CATEGORY_TITLE = "N"

    def __init__(self, color_pk: str) -> None:
        super().__init__(color_pk, Necklace.CATEGORY_TITLE)


class Ring(ProductMixin):
    CATEGORY_TITLE = "R"

    def __init__(self, color_pk: str) -> None:
        super().__init__(color_pk, Ring.CATEGORY_TITLE)


"""
Each Concrete Factory has a corresponding product variant.
"""


class PinkProductSetFactory(AbstractProductSetFactory):
    COLOR_PK = Color.objects.get(title="P").pk

    def create_earring(self):
        return Earring(PinkProductSetFactory.COLOR_PK).get_product()

    def create_bracelet(self):
        return Bracelet(PinkProductSetFactory.COLOR_PK).get_product()

    def create_necklace(self):
        return Necklace(PinkProductSetFactory.COLOR_PK).get_product()

    def create_ring(self):
        return Ring(PinkProductSetFactory.COLOR_PK).get_product()

    def generate_product_set(self):
        earring = self.create_earring()
        bracelet = self.create_bracelet()
        necklace = self.create_necklace()
        ring = self.create_ring()

        return [earring, bracelet, necklace, ring]


class BlueProductSetFactory(AbstractProductSetFactory):
    COLOR_PK = Color.objects.get(title="B").pk

    def create_earring(self):
        return Earring(BlueProductSetFactory.COLOR_PK).get_product()

    def create_bracelet(self):
        return Bracelet(BlueProductSetFactory.COLOR_PK).get_product()

    def create_necklace(self):
        return Necklace(BlueProductSetFactory.COLOR_PK).get_product()

    def create_ring(self):
        return Ring(BlueProductSetFactory.COLOR_PK).get_product()

    def generate_product_set(self):
        earring = self.create_earring()
        bracelet = self.create_bracelet()
        necklace = self.create_necklace()
        ring = self.create_ring()

        return [earring, bracelet, necklace, ring]


class WhiteProductSetFactory(AbstractProductSetFactory):
    COLOR_PK = Color.objects.get(title="W").pk

    def create_earring(self):
        return Earring(WhiteProductSetFactory.COLOR_PK).get_product()

    def create_bracelet(self):
        return Bracelet(WhiteProductSetFactory.COLOR_PK).get_product()

    def create_necklace(self):
        return Necklace(WhiteProductSetFactory.COLOR_PK).get_product()

    def create_ring(self):
        return Ring(WhiteProductSetFactory.COLOR_PK).get_product()

    def generate_product_set(self):
        earring = self.create_earring()
        bracelet = self.create_bracelet()
        necklace = self.create_necklace()
        ring = self.create_ring()

        return [earring, bracelet, necklace, ring]
