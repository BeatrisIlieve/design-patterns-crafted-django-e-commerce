# Generated by Django 5.1.3 on 2024-12-03 13:39

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_credential_details', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserShippingDetails',
            fields=[
                ('first_name', models.CharField(error_messages={'blank': 'This field is required', 'max_length': 'This field must not exceed 255 characters'}, max_length=255, validators=[django.core.validators.MinLengthValidator(limit_value=2, message='This field must be at least 2 characters long'), django.core.validators.RegexValidator(message='First Name can only contain letters, spaces, hyphens, and must start and end with a letter', regex='(^[A-Za-z]{2,}$)|(^[A-Za-z]{1,}[\\s\\-]?[A-Za-z]{1,}$)')])),
                ('last_name', models.CharField(error_messages={'blank': 'This field is required', 'max_length': 'This field must not exceed 255 characters'}, max_length=255, validators=[django.core.validators.MinLengthValidator(limit_value=2, message='This field must be at least 2 characters long'), django.core.validators.RegexValidator(message='Last Name can only contain letters, spaces, hyphens, and must start and end with a letter', regex='(^[A-Za-z]{2,}$)|(^[A-Za-z]{1,}[\\s\\-]?[A-Za-z]{1,}$)')])),
                ('phone_number', models.CharField(error_messages={'blank': 'This field is required', 'max_length': 'This field must not exceed 15 characters'}, max_length=15, validators=[django.core.validators.MinLengthValidator(limit_value=7, message='This field must be at least 7 characters long'), django.core.validators.RegexValidator(message='This field can only contain digits', regex='^[0-9]+$')])),
                ('country', models.CharField(error_messages={'blank': 'This field is required', 'max_length': 'This field must not exceed 255 characters'}, max_length=255, validators=[django.core.validators.MinLengthValidator(limit_value=2, message='This field must be at least 2 characters long'), django.core.validators.RegexValidator(message='Country Name can only contain letters, spaces, hyphens, and must start and end with a letter', regex='(^[A-Za-z]{2,}$)|(^[A-Za-z]{1,}[\\s\\-]?[A-Za-z]{1,}$)')])),
                ('city', models.CharField(error_messages={'blank': 'This field is required', 'max_length': 'This field must not exceed 255 characters'}, max_length=255, validators=[django.core.validators.MinLengthValidator(limit_value=2, message='This field must be at least 2 characters long'), django.core.validators.RegexValidator(message='City Name can only contain letters, spaces, hyphens, and must start and end with a letter', regex='(^[A-Za-z]{2,}$)|(^[A-Za-z]{1,}[\\s\\-]?[A-Za-z]{1,}$)')])),
                ('street_address', models.CharField(error_messages={'blank': 'This field is required', 'max_length': 'This field must not exceed 255 characters'}, max_length=255, validators=[django.core.validators.MinLengthValidator(limit_value=8, message='This field must be at least 8 characters long'), django.core.validators.RegexValidator(message='This field can only contain letters, spaces, hyphens, apostrophes, and periods, and must start and end with a letter or digit', regex="^([A-Za-z0-9]{1,})([A-Za-z0-9\\s\\-\\.']{6,})([A-Za-z0-9])$")])),
                ('apartment', models.CharField(blank=True, error_messages={'blank': 'This field is required', 'max_length': 'This field must not exceed 10 characters'}, max_length=10, null=True, validators=[django.core.validators.MinLengthValidator(limit_value=1, message='This field must be at least 1 characters long'), django.core.validators.RegexValidator(message='This field can only contain letters, spaces, hyphens, and periods, and must start and end with a letter or digit', regex='^([A-Za-z0-9]{1,5})([A-Za-z0-9\\s\\-\\.]{0,4})([A-Za-z0-9]?)$')])),
                ('postal_code', models.CharField(error_messages={'blank': 'This field is required', 'max_length': 'This field must not exceed 15 characters'}, max_length=15, validators=[django.core.validators.MinLengthValidator(limit_value=3, message='This field must be at least 3 characters long'), django.core.validators.RegexValidator(message='This field can only contain letters, spaces, hyphens, commas, and periods, and must start and end with a letter or digit', regex='^([A-Za-z0-9]{1,})([A-Za-z0-9\\s\\-\\.\\,]{0,12})([A-Za-z0-9]{1})$')])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='shipping_details', serialize=False, to='user_credential_details.usercredentialdetails')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
