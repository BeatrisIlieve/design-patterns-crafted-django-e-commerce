from django.db import (
    models,
)


class InventoryManager(models.Manager):
    def get_product_into_products_list(self, category_pk, color_pk):
        return self.filter(
            product__category_id=category_pk,
            product__color_id=color_pk,
        ).select_related(
            "product", "product__category", "product__color"
        )
                
    def get_product_into_product_page(self):
        pass
