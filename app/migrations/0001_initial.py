# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CelebrityContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('headline', models.CharField(max_length=300)),
                ('img', models.URLField(blank=True, null=True)),
                ('url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FashionContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('headline', models.CharField(max_length=300)),
                ('img', models.URLField(blank=True, null=True)),
                ('url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FinanceContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('headline', models.CharField(max_length=300)),
                ('img', models.URLField(blank=True, null=True)),
                ('url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PoliticsContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('headline', models.CharField(max_length=300)),
                ('img', models.URLField(blank=True, null=True)),
                ('url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ReceipesContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('headline', models.CharField(max_length=300)),
                ('img', models.URLField(blank=True, null=True)),
                ('url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SportsContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('headline', models.CharField(max_length=300)),
                ('img', models.URLField(blank=True, null=True)),
                ('url', models.TextField()),
            ],
        ),
    ]
