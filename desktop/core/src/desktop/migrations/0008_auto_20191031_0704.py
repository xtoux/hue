# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-10-31 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desktop', '0007_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defaultconfiguration',
            name='properties',
            field=models.TextField(default='[]', help_text='JSON-formatted default properties values.'),
        ),
    ]