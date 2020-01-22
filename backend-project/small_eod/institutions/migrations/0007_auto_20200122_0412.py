# Generated by Django 3.0.2 on 2020-01-22 04:12

import django.core.validators
from django.db import migrations, models
import small_eod.generic.validators


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0006_auto_20200122_0335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='externalidentifier',
            name='nip',
            field=models.CharField(blank=True, max_length=10, null=True, validators=[small_eod.generic.validators.ExactLengthsValidator([10]), django.core.validators.RegexValidator('^[0-9]*$')]),
        ),
        migrations.AlterField(
            model_name='externalidentifier',
            name='regon',
            field=models.CharField(blank=True, max_length=14, null=True, validators=[small_eod.generic.validators.ExactLengthsValidator([10, 14]), django.core.validators.RegexValidator('^[0-9]*$')]),
        ),
    ]
