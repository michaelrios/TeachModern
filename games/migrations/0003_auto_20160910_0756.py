# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-10 07:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_auto_20160910_0745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameseed',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date soft deleted'),
        ),
    ]
