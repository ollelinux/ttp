# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-19 20:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='first_name',
            field=models.CharField(db_index=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='last_name',
            field=models.CharField(db_index=True, max_length=255),
        ),
    ]
