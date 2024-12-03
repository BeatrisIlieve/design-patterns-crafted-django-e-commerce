# Generated by Django 5.1.3 on 2024-12-03 15:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
        ('shopping_bag', '0002_initial'),
        ('user_credential_details', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shoppingbag',
            options={},
        ),
        migrations.AlterField(
            model_name='shoppingbag',
            name='inventory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.inventory'),
        ),
        migrations.AlterField(
            model_name='shoppingbag',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_credential_details.usercredentialdetails'),
        ),
    ]