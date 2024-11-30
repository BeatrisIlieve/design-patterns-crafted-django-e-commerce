import os
import django
from django.core.management.base import (
    BaseCommand,
)

from design_patterns_crafted_django_e_commerce.product.models import (
    Category,
    Color,
    Product,
)


class Command(BaseCommand):
    help = "Initialize data for your Django app"

    def handle(self, *args, **options):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_gems.settings")
        django.setup()

        self.stdout.write(self.style.SUCCESS("Starting data initialization..."))

        self.bulk_create_category()

        self.bulk_create_color()

        self.bulk_create_product()

        self.stdout.write(
            self.style.SUCCESS("Data initialization completed successfully.")
        )

    def bulk_create_category(self):
        Category.objects.bulk_create(
            [
                Category(title=Category.TITLE_CHOICES[0][0]),
                Category(title=Category.TITLE_CHOICES[1][0]),
                Category(title=Category.TITLE_CHOICES[2][0]),
                Category(title=Category.TITLE_CHOICES[3][0]),
            ]
        )

    def bulk_create_color(self):
        Color.objects.bulk_create(
            [
                Color(title=Color.TITLE_CHOICES[0][0]),
                Color(title=Color.TITLE_CHOICES[1][0]),
                Color(title=Color.TITLE_CHOICES[2][0]),
            ]
        )

    def bulk_create_product(self):
        categories = Category.objects.all()
        colors = Color.objects.all()

        Product.objects.bulk_create(
            [
                Product(
                    first_image_url="https://res.cloudinary.com/deztgvefu/image/upload/v1723714885/forget-me-not-collection/earrings/forget_me_not_drop_earrings_diamond_and_pink_sapphire_eapspdrflrfmn_ee-1_zzaw4q.webp",
                    second_image_url="https://res.cloudinary.com/deztgvefu/image/upload/v1723714886/forget-me-not-collection/earrings/forget_me_not_drop_earrings_diamond_and_pink_sapphire_eapspdrflrfmn_ee-2_p9jicb.webp",
                    category=categories[0],
                    color=colors[0],
                    description="28 pear-shaped and round brilliant sapphires weighing a total of approximately 3.20 carats and 28 marquise and round brilliant diamonds weighing a total of approximately 1.98 carats, set in platinum.",
                ),
                Product(
                    first_image_url="https://res.cloudinary.com/deztgvefu/image/upload/v1723714886/forget-me-not-collection/earrings/forget_me_not_drop_earrings_diamond_and_sapphire_easpdrflrfmn_ee-1_zx2cga.webp",
                    second_image_url="https://res.cloudinary.com/deztgvefu/image/upload/v1723714886/forget-me-not-collection/earrings/forget_me_not_drop_earrings_diamond_and_sapphire_easpdrflrfmn_ee-2_vtkyhb.webp",
                    category=categories[0],
                    color=colors[1],
                    description="28 pear-shaped and round brilliant sapphires weighing a total of approximately 3.00 carats and 28 marquise and round brilliant diamonds weighing a total of approximately 1.98 carats, set in platinum.",
                ),
                Product(
                    first_image_url="https://res.cloudinary.com/deztgvefu/image/upload/v1723714890/forget-me-not-collection/earrings/forget_me_not_diamond_drop_earrings_eadpdrflrfmn_ee-1_knlt2u.webp",
                    second_image_url="https://res.cloudinary.com/deztgvefu/image/upload/v1723714886/forget-me-not-collection/earrings/forget_me_not_diamond_drop_earrings_eadpdrflrfmn_ee-2_sksk7o.webp",
                    category=categories[0],
                    color=colors[2],
                    description="A medley of marquise, pear-shaped, and round brilliant diamonds, weighing a total of approximately 4.38 carats, set in platinum.",
                ),
                Product(
                    first_image_url="https://res.cloudinary.com/deztgvefu/image/upload/v1723714894/forget-me-not-collection/bracelets/forget_me_not_bracelet_diamond_and_pink_sapphire_brpsprfflrfmn_e_1_vz9pv4.avif",
                    second_image_url="https://res.cloudinary.com/deztgvefu/image/upload/v1723714893/forget-me-not-collection/bracelets/forget_me_not_bracelet_diamond_and_pink_sapphire_brpsprfflrfmn_e_2_kdpnm6.avif",
                    category=categories[1],
                    color=colors[0],
                    description="45 pear-shaped and round brilliant sapphires weighing a total of approximately 4.36 carats and 33 pear-shaped, marquise and round brilliant diamonds weighing a total of approximately 4.24 carats, set in platinum.",
                ),
                Product(
                    first_image_url="https://res.cloudinary.com/deztgvefu/image/upload/v1723714894/forget-me-not-collection/bracelets/forget_me_not_bracelet_diamond_and_sapphire_brsprfflrfmn_e_1_fokzrw.webp",
                    second_image_url="https://res.cloudinary.com/deztgvefu/image/upload/v1723714895/forget-me-not-collection/bracelets/forget_me_not_bracelet_diamond_and_sapphire_brsprfflrfmn_e_2_ojfbze.avif",
                    category=categories[1],
                    color=colors[1],
                    description="45 pear-shaped and round brilliant sapphires weighing a total of approximately 4.17 carats and 33 pear-shaped, marquise and round brilliant diamonds weighing a total of approximately 4.24 carats, set in platinum.",
                ),
                Product(
                    first_image_url="https://res.cloudinary.com/deztgvefu/image/upload/v1723714893/forget-me-not-collection/bracelets/forget_me_not_diamond_bracelet_brdprfflrfmn_e-1_muieri.avif",
                    second_image_url="https://res.cloudinary.com/deztgvefu/image/upload/v1723714894/forget-me-not-collection/bracelets/forget_me_not_bracelet_diamond_and_pink_sapphire_brpsprfflrfmn_e_2_1_pvbpcb.png",
                    category=categories[1],
                    color=colors[2],
                    description="78 pear-shaped, marquise, and round brilliant diamonds, weighing a total of approximately 7.46 carats, set in platinum.",
                ),
                Product(
                    first_image_url="https://res.cloudinary.com/deztgvefu/image/upload/v1723714890/forget-me-not-collection/necklaces/forget_me_not_lariat_necklace_diamond_and_pink_sapphire_nkpspltflrfmn_e_1_kuxbds.webp",
                    second_image_url="https://res.cloudinary.com/deztgvefu/image/upload/v1723714890/forget-me-not-collection/necklaces/forget_me_not_lariat_necklace_diamond_and_pink_sapphire_nkpspltflrfmn_e_2_d2fc78.webp",
                    category=categories[2],
                    color=colors[0],
                    description="78 pear-shaped and round brilliant sapphires weighing a total of approximately 8.61 carats and 99 marquise and round brilliant diamonds weighing a total of approximately 8.60 carats, set in platinum.",
                ),
                Product(
                    first_image_url="https://res.cloudinary.com/deztgvefu/image/upload/v1723714891/forget-me-not-collection/necklaces/forget_me_not_lariat_necklace_diamond_and_sapphire_nkspltflrfmn_e_1_p2uxlj.webp",
                    second_image_url="https://res.cloudinary.com/deztgvefu/image/upload/v1723714890/forget-me-not-collection/necklaces/forget_me_not_lariat_necklace_diamond_and_sapphire_nkspltflrfmn_e_2_hxgdcy.avif",
                    category=categories[2],
                    color=colors[1],
                    description="78 pear-shaped and round brilliant sapphires weighing a total of approximately 8.61 carats and 99 marquise and round brilliant diamonds weighing a total of approximately 8.37 carats, set in platinum.",
                ),
                Product(
                    first_image_url="https://res.cloudinary.com/deztgvefu/image/upload/v1723714886/forget-me-not-collection/necklaces/forget_me_not_lariat_diamond_necklace_nkdpltflrfmn_e-1_u0gwpv.avif",
                    second_image_url="https://res.cloudinary.com/deztgvefu/image/upload/v1723714891/forget-me-not-collection/necklaces/forget_me_not_lariat_diamond_necklace_nkdpltflrfmn_e-2_tuh8ru.webp",
                    category=categories[2],
                    color=colors[2],
                    description="177 pear-shaped, marquise, and round brilliant diamonds, weighing a total of approximately 15.35 carats, set in platinum.",
                ),
                Product(
                    first_image_url="https://res.cloudinary.com/deztgvefu/image/upload/v1723714892/forget-me-not-collection/rings/forget_me_not_ring_diamond_and_pink_sapphire_frpsprfflrfmn_e_1_qfumu3.webp",
                    second_image_url="https://res.cloudinary.com/deztgvefu/image/upload/v1723714892/forget-me-not-collection/rings/forget_me_not_ring_diamond_and_pink_sapphire_frpsprfflrfmn_e_2_k7nhpe.avif",
                    category=categories[3],
                    color=colors[0],
                    description="6 pear-shaped sapphires weighing a total of approximately 2.22 carats and 1 round brilliant diamond weighing approximately 0.05 carats, set in platinum.",
                ),
                Product(
                    first_image_url="https://res.cloudinary.com/deztgvefu/image/upload/v1723714893/forget-me-not-collection/rings/forget_me_not_ring_diamond_and_sapphire_frsprfflrfmn_e_1_pm9u6t.avif",
                    second_image_url="https://res.cloudinary.com/deztgvefu/image/upload/v1723714891/forget-me-not-collection/rings/forget_me_not_ring_diamond_and_sapphire_frsprfflrfmn_e_2_ucppcd.avif",
                    category=categories[3],
                    color=colors[1],
                    description="6 pear-shaped sapphires weighing a total of approximately 2.15 carats and 1 round brilliant diamond weighing approximately 0.05 carats, set in platinum.",
                ),
                Product(
                    first_image_url="https://res.cloudinary.com/deztgvefu/image/upload/v1723714891/forget-me-not-collection/rings/forget_me_not_diamond_ring_frdprfflrfmn_e-1h_yueh2k.webp",
                    second_image_url="https://res.cloudinary.com/deztgvefu/image/upload/v1723714891/forget-me-not-collection/rings/forget_me_not_diamond_ring_frdprfflrfmn_e-2h_mktny9.webp",
                    category=categories[3],
                    color=colors[2],
                    description="6 pear-shaped and 1 round brilliant diamond, weighing a total of approximately 1.66 carats, set in platinum.",
                ),
            ]
        )
