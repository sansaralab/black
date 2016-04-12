# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-12 18:53
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identity', models.TextField()),
                ('title', models.TextField()),
                ('content', models.TextField()),
                ('likes', models.IntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='complaints_manager.Category')),
            ],
        ),
        migrations.CreateModel(
            name='PersonSummary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identity', models.TextField(unique=True)),
                ('complaints', django.contrib.postgres.fields.ArrayField(base_field=models.BigIntegerField(), blank=True, size=None)),
            ],
        ),
    ]
