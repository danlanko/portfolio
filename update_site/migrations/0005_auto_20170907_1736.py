# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-07 16:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('update_site', '0004_auto_20170907_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='testimony'),
        ),
    ]
