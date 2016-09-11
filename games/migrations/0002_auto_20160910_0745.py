# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-10 07:45
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameSeed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(verbose_name='date created')),
                ('updated_at', models.DateTimeField(verbose_name='date last updated')),
                ('deleted_at', models.DateTimeField(verbose_name='date soft deleted')),
            ],
        ),
        migrations.RemoveField(
            model_name='codewords',
            name='owner',
        ),
        migrations.CreateModel(
            name='CodeWordsSeed',
            fields=[
                ('gameseed_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='games.GameSeed')),
                ('words', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
            bases=('games.gameseed',),
        ),
        migrations.DeleteModel(
            name='CodeWords',
        ),
        migrations.AddField(
            model_name='gameseed',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]