# Generated by Django 5.1.3 on 2024-12-02 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_bag', '0003_shoppingbag_created_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shoppingbag',
            options={'ordering': ('created_at',)},
        ),
    ]
