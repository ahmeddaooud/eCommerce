# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-28 14:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20180426_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='billing_address_final',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_address_final',
            field=models.TextField(blank=True, null=True),
        ),
    ]