# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-23 20:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20180423_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taggedarticle',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tag_items', to='articles.ArticleTag'),
        ),
    ]
