"""
1. Set up a PostgreSQL database
2. Set up django-cities
3. Run python manage.py makemigrations
4. Run python manage.py migrate
5. Run python manage.py initialize_products_data
6. Run python manage.py initialize_inventory_data
7. Run the current file
8. Compare the result with the output at the bottom of the current file
"""

import os
import django


os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "design_patterns_crafted_django_e_commerce.settings"
)
django.setup()


from cities_light.models import (
    Country,
    City,
    Region,
)

from django.core.exceptions import (
    ValidationError,
)

from design_patterns_crafted_django_e_commerce.user_credential_details.models import (
    UserCredentialDetails,
)

from design_patterns_crafted_django_e_commerce.product.models import (
    Category,
    Color,
)

from design_patterns_crafted_django_e_commerce.wishlist.models import (
    Wishlist,
)
from design_patterns_crafted_django_e_commerce.shopping_bag.models import (
    ShoppingBag,
)
from design_patterns_crafted_django_e_commerce.inventory.models import (
    Inventory,
)
from design_patterns_crafted_django_e_commerce.wishlist.models import (
    Wishlist,
)

from design_patterns_crafted_django_e_commerce.user_delivery.facade import (
    DeliveryFacade,
    UpdateUserShippingDetails,
    CreateUserOrder,
    CreateUserDelivery,
    client_code_delivery,
)

from design_patterns_crafted_django_e_commerce.order.facade import (
    UpdateUserPaymentDetails,
    MoveShoppingBagItemsToOrderItem,
    GenerateOrderConfirmation,
    OrderFacade,
    client_code_order,
)


class TestEntireFunctionality:
    def __init__(self) -> None:
        self.__user_email: str = "beatrisilieve@icloud.com"
        self.__user_password: str = "123456Aa@"
        self.__category_pk_1: int = Category.objects.get(title="E").pk
        self.__color_pk_1: int = Color.objects.get(title="P").pk
        self.__category_pk_2: int = Category.objects.get(title="B").pk
        self.__color_pk_2: int = Color.objects.get(title="B").pk
        self.__user: UserCredentialDetails = None

    def __test_register_user(self) -> str:
        try:
            user = UserCredentialDetails.objects.create(
                email=self.__user_email, password=self.__user_password
            )

            self.__user = user

            return f"User with email {self.__user_email} has successfully registered."
        except ValidationError as e:
            return e.messages[0]

    def __test_register_user_with_duplicate_email(self) -> str:
        try:
            UserCredentialDetails.objects.create(
                email=self.__user_email, password=self.__user_password
            )
            return f"User with email {self.__user_email} has successfully registered."
        except ValidationError as e:
            return e.messages[0]

    def __test_get_product_into_products_list_page(self):
        inventories = Inventory.objects.get_product_into_products_list(
            self.__category_pk_1, self.__color_pk_1
        )

        is_liked_by_user = Wishlist.objects.check_if_a_product_is_liked_by_user(
            inventories[0]["product_id"], self.__user
        )

        result = "\n\n".join(
            [
                "Product details into products list page:",
                f"First image: {inventories[0]['product__first_image_url']}",
                f"Second image: {inventories[0]['product__second_image_url']}",
                f"Category: {inventories[0]['full_category_title']}",
                f"Color: {inventories[0]['full_color_title']}",
                f"Price range: {inventories[0]['min_price']} - {inventories[0]['max_price']}",
                f"Availability: {inventories[0]['is_sold_out']}",
                f"Is liked by user: {is_liked_by_user}",
            ]
        )

        return result

    def __test_get_product_into_product_page(self) -> str:

        inventories = Inventory.objects.get_product_into_product_page(
            self.__category_pk_1, self.__color_pk_1
        )

        is_liked_by_user = Wishlist.objects.check_if_a_product_is_liked_by_user(
            inventories[0]["product_id"], self.__user
        )

        inventory_details = inventories[0]["inventory_details"]

        sizes_by_inventory_id_and_price = []

        for item in inventory_details:
            for key, value in item.items():
                sizes_by_inventory_id_and_price.append(f"{key}: {value}")
            sizes_by_inventory_id_and_price.append("\n")

        result = "\n\n".join(
            [
                "Product details into products list page:",
                f"First image: {inventories[0]['product__first_image_url']}",
                f"Second image: {inventories[0]['product__second_image_url']}",
                f"Description: {inventories[0]['product__description']}",
                f"Category: {inventories[0]['full_category_title']}",
                f"Color: {inventories[0]['full_color_title']}",
                f"Availability: {inventories[0]['is_sold_out']}",
                f"Is liked by user: {is_liked_by_user}",
                "\n".join(sizes_by_inventory_id_and_price),
            ]
        )

        return result

    def __test_execute_clicking_on_the_like_button(self):
        inventories = Inventory.objects.get_product_into_products_list(
            self.__category_pk_1, self.__color_pk_1
        )

        is_liked_by_user = Wishlist.objects.check_if_a_product_is_liked_by_user(
            inventories[0]["product_id"], self.__user
        )

        if is_liked_by_user:
            return Wishlist.objects.remove_product_from_wishlist(
                inventories[0]["product_id"], self.__user
            )

        return Wishlist.objects.add_product_to_wishlist(
            inventories[0]["product_id"], self.__user
        )

    def __test_get_products_in_user_wishlist(self):
        inventories = Wishlist.objects.get_all_liked_products(self.__user)

        result = []

        for inventory in inventories:
            result.extend(
                [
                    "\n",
                    "Product details into user wishlist page:",
                    f"First image: {inventory[0]['product__first_image_url']}",
                    f"Second image: {inventory[0]['product__second_image_url']}",
                    f"Category: {inventory[0]['full_category_title']}",
                    f"Color: {inventory[0]['full_color_title']}",
                    f"Price range: {inventory[0]['min_price']} - {inventory[0]['max_price']}",
                    f"Availability: {inventory[0]['is_sold_out']}",
                ]
            )

        return "\n\n".join(result)

    def __test_execute_clicking_on_the_add_to_bag_button(self, category_pk, color_pk):
        inventories = Inventory.objects.get_product_into_product_page(
            category_pk, color_pk
        )

        inventory_pk = inventories[0]["inventory_details"][0]["inventory_id"]

        return ShoppingBag.objects.add_item(inventory_pk, self.__user)

    def __test_increase_shopping_bag_quantity(self):
        inventories = Inventory.objects.get_product_into_product_page(
            self.__category_pk_1, self.__color_pk_1
        )

        inventory_pk = inventories[0]["inventory_details"][0]["inventory_id"]

        return ShoppingBag.objects.increase_item_quantity(inventory_pk, self.__user)

    def __test_decrease_shopping_bag_quantity(self):
        inventories = Inventory.objects.get_product_into_product_page(
            self.__category_pk_1, self.__color_pk_1
        )

        inventory_pk = inventories[0]["inventory_details"][0]["inventory_id"]

        return ShoppingBag.objects.decrease_item_quantity(inventory_pk, self.__user)

    def __test_get_all_shopping_bag_items_per_user(self):
        bag_items = ShoppingBag.objects.get_all_shopping_bag_items_per_user(self.__user)

        result = []

        total_bag_price = bag_items[0]["total_bag_sum"]

        result.append(f"Total bag price: {total_bag_price}")

        for bag_item in bag_items:
            result.append(f"First image: {bag_item['first_image']}")
            result.append(f"Color: {bag_item['full_color_title']}")
            result.append(f"Category: {bag_item['full_category_title']}")
            result.append(f"Quantity: {bag_item['quantity']}")
            result.append(f"Total price per item: {bag_item['total_per_item']}")

        return "\n\n".join(result)

    def __test_clicking_on_continue_checkout_button(self):
        country = Country.objects.get(name="Bulgaria")
        region = Region.objects.get(name="Sofia-Capital")
        city = City.objects.get(name="Sofia")

        shipping_details = {
            "first_name": "Beatris",
            "last_name": "Ilieva",
            "phone_number": "1234567890",
            "country": country,
            "city": city,
            "region": region,
            "street_address": "Some Street 1",
            "apartment": "Apt. 1",
            "postal_code": "1000",
        }

        update_user_shipping_details = UpdateUserShippingDetails()
        create_user_order = CreateUserOrder()
        create_user_delivery = CreateUserDelivery()
        facade = DeliveryFacade(
            update_user_shipping_details, create_user_order, create_user_delivery
        )
        method_choice = "EH"

        return client_code_delivery(
            facade, self.__user.pk, method_choice, shipping_details
        )

    def __test_clicking_on_process_payment_button(self):
        payment_details = {
            "card_holder": "Beatris Ilieva",
            "card_number": "1234567890123457",
            "expiry_month": "05",
            "expiry_year": "2026",
            "cvv_code": "123",
        }

        update_user_payment_details = UpdateUserPaymentDetails()
        move_shopping_bag_item_to_order_item = MoveShoppingBagItemsToOrderItem()
        generate_order_confirmation = GenerateOrderConfirmation()

        facade = OrderFacade(
            update_user_payment_details,
            move_shopping_bag_item_to_order_item,
            generate_order_confirmation,
        )

        order_confirmation_data = client_code_order(
            facade, self.__user.pk, payment_details
        )

        result = [
            "\n",
            "Order Confirmation:",
        ]

        delivery_method = f"Delivery Method: {order_confirmation_data[0]['delivery_method_full_title']}"
        total_order_cost = (
            f"Total Order Cost: {order_confirmation_data[0]['delivery__total_cost']}"
        )
        delivery_due_date = (
            f"Delivery Due Date: {order_confirmation_data[0]['delivery__due_date']}"
        )
        created_at = f"Created at: {order_confirmation_data[0]['created_date']}"

        result.append(delivery_method)
        result.append(total_order_cost)
        result.append(delivery_due_date)
        result.append(created_at)

        for index, data in enumerate(order_confirmation_data):
            result.extend(
                [
                    f"Item {index + 1}:",
                    f"Item quantity: {data['order_item_order__quantity']}",
                    f"Item Price: {data['order_item_order__inventory__price']}",
                    f"Total Price Per Item: {data['total_price_per_product']}",
                    f"Item Size: {data['order_item_order__inventory__size']}",
                    f"Item Image: {data['order_item_order__inventory__product__first_image_url']}",
                ]
            )

        return "\n\n".join(result)

    def execute(self):
        result = []

        result.append(self.__test_register_user())
        result.append(self.__test_register_user_with_duplicate_email())
        result.append(self.__test_get_product_into_products_list_page())
        result.append(self.__test_get_product_into_product_page())
        result.append(self.__test_execute_clicking_on_the_like_button())
        result.append(self.__test_get_products_in_user_wishlist())
        result.append(
            self.__test_execute_clicking_on_the_add_to_bag_button(
                self.__category_pk_1, self.__color_pk_1
            )
        )
        result.append(
            self.__test_execute_clicking_on_the_add_to_bag_button(
                self.__category_pk_2, self.__color_pk_2
            )
        )
        result.append(self.__test_increase_shopping_bag_quantity())
        result.append(self.__test_increase_shopping_bag_quantity())
        result.append(self.__test_decrease_shopping_bag_quantity())
        result.append(self.__test_get_all_shopping_bag_items_per_user())
        result.append(self.__test_clicking_on_continue_checkout_button())
        result.append(self.__test_clicking_on_process_payment_button())
        return "\n\n".join(result)


instance = TestEntireFunctionality()

print(instance.execute())

# OUTPUT:
"""
User with email beatrisilieve@icloud.com has successfully registered. 

User with that email address already exists

Product details into products list page:

First image: https://res.cloudinary.com/deztgvefu/image/upload/v1723714885/forget-me-not-collection/earrings/forget_me_not_drop_earrings_diamond_and_pink_sapphire_eapspdrflrfmn_ee-1_zzaw4q.webp

Second image: https://res.cloudinary.com/deztgvefu/image/upload/v1723714886/forget-me-not-collection/earrings/forget_me_not_drop_earrings_diamond_and_pink_sapphire_eapspdrflrfmn_ee-2_p9jicb.webp

Category: Earrings

Color: Pink

Price range: 43000.00 - 45000.00

Availability: In Stock

Is liked by user: False

Product details into products list page:

First image: https://res.cloudinary.com/deztgvefu/image/upload/v1723714885/forget-me-not-collection/earrings/forget_me_not_drop_earrings_diamond_and_pink_sapphire_eapspdrflrfmn_ee-1_zzaw4q.webp

Second image: https://res.cloudinary.com/deztgvefu/image/upload/v1723714886/forget-me-not-collection/earrings/forget_me_not_drop_earrings_diamond_and_pink_sapphire_eapspdrflrfmn_ee-2_p9jicb.webp

Description: 28 pear-shaped and round brilliant sapphires weighing a total of approximately 3.20 carats and 28 marquise and round brilliant diamonds weighing a total of approximately 1.98 carats, set in platinum.

Category: Earrings

Color: Pink

Availability: In Stock

Is liked by user: False

size: 4.05
price: 43000.00
inventory_id: 1
stock_status: In Stock


size: 4.98
price: 44000.00
inventory_id: 2
stock_status: In Stock


size: 5.86
price: 45000.00
inventory_id: 3
stock_status: In Stock



Product has been added to wishlist




Product details into user wishlist page:

First image: https://res.cloudinary.com/deztgvefu/image/upload/v1723714885/forget-me-not-collection/earrings/forget_me_not_drop_earrings_diamond_and_pink_sapphire_eapspdrflrfmn_ee-1_zzaw4q.webp

Second image: https://res.cloudinary.com/deztgvefu/image/upload/v1723714886/forget-me-not-collection/earrings/forget_me_not_drop_earrings_diamond_and_pink_sapphire_eapspdrflrfmn_ee-2_p9jicb.webp

Category: Earrings

Color: Pink

Price range: 43000.00 - 45000.00

Availability: In Stock

Item has been added to shopping bag

Item has been added to shopping bag

Quantity has been increased

Quantity has been increased

Quantity has been decreased

Total bag price: 120000.00

First image: https://res.cloudinary.com/deztgvefu/image/upload/v1723714894/forget-me-not-collection/bracelets/forget_me_not_bracelet_diamond_and_sapphire_brsprfflrfmn_e_1_fokzrw.webp

Color: Blue

Category: Bracelets

Quantity: 1

Total price per item: 34000.00

First image: https://res.cloudinary.com/deztgvefu/image/upload/v1723714885/forget-me-not-collection/earrings/forget_me_not_drop_earrings_diamond_and_pink_sapphire_eapspdrflrfmn_ee-1_zzaw4q.webp

Color: Pink

Category: Earrings

Quantity: 2

Total price per item: 86000.00

User Shipping Details have been successfully updated




Order Confirmation:

Delivery Method: Express Home

Total Order Cost: 120030.00

Delivery Due Date: 2024-12-06

Created at: 2024-12-04

Item 1:

Item quantity: 1

Item Price: 34000.00

Total Price Per Item: 34000.00

Item Size: 15.02

Item Image: https://res.cloudinary.com/deztgvefu/image/upload/v1723714894/forget-me-not-collection/bracelets/forget_me_not_bracelet_diamond_and_sapphire_brsprfflrfmn_e_1_fokzrw.webp

Item 2:

Item quantity: 2

Item Price: 43000.00

Total Price Per Item: 86000.00

Item Size: 4.05

Item Image: https://res.cloudinary.com/deztgvefu/image/upload/v1723714885/forget-me-not-collection/earrings/forget_me_not_drop_earrings_diamond_and_pink_sapphire_eapspdrflrfmn_ee-1_zzaw4q.webp
"""

