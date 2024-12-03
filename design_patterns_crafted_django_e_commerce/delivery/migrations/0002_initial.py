# Generated by Django 5.1.3 on 2024-12-03 16:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('delivery', '0001_initial'),
        ('order', '0004_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order'),
        ),
    ]
