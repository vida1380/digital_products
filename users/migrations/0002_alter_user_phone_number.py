# Generated by Django 5.2 on 2025-06-06 16:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.BigIntegerField(blank=True, error_messages={'unique': 'A user with that username already exits.'}, null=True, unique=True, validators=[django.core.validators.RegexValidator('^989[0-,9]\\d{8}&', 'Enter a valid mobile number. ')], verbose_name='mobile number'),
        ),
    ]
