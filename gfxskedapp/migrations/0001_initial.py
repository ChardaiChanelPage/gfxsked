# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-11 17:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requestorName', models.CharField(max_length=50)),
                ('contactName', models.CharField(max_length=50)),
                ('contactEmail', models.EmailField(max_length=254)),
                ('publishDate', models.CharField(max_length=50)),
                ('details', models.CharField(max_length=500)),
                ('isExistingArticle', models.CharField(max_length=3)),
                ('providedURL', models.CharField(max_length=50)),
                ('slug', models.CharField(max_length=10)),
                ('isAssigned', models.CharField(max_length=3)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
    ]
