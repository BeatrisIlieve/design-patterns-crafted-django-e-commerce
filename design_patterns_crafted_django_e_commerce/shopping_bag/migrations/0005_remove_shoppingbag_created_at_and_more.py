# Generated by Django 5.1.3 on 2024-12-04 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_bag', '0004_alter_shoppingbag_unique_together_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppingbag',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='shoppingbag',
            name='inventory',
        ),
        migrations.RemoveField(
            model_name='shoppingbag',
            name='quantity',
        ),
    ]