# Generated by Django 5.1.3 on 2024-12-03 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_orderitem_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='orderitem',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='inventory',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='user',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]
