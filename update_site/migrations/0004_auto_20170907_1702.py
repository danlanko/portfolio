# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-07 16:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('update_site', '0003_testimonial_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='image',
            field=models.ImageField(blank=True, upload_to='testimony'),
        ),
    ]
