# Generated by Django 5.1.3 on 2024-12-03 15:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities_light', '0011_alter_city_country_alter_city_region_and_more'),
        ('user_shipping_details', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usershippingdetails',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cities_light.region'),
        ),
        migrations.AlterField(
            model_name='usershippingdetails',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cities_light.city'),
        ),
        migrations.AlterField(
            model_name='usershippingdetails',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cities_light.country'),
        ),
    ]
