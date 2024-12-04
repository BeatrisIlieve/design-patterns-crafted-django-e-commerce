from django.core.exceptions import (
    ValidationError,
)

from design_patterns_crafted_django_e_commerce.user_payment_details.models import (
    UserPaymentDetails,
)
from design_patterns_crafted_django_e_commerce.shopping_bag.models import (ShoppingBag,)
from design_patterns_crafted_django_e_commerce.order.models import(Order, OrderItem,)

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
        
            OrderItem.objects.create(order=order, inventory=inventory, quantity=quantity)
            
            bag_item.delete()
        
        
