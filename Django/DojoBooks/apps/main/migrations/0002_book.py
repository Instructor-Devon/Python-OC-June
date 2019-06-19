# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-06-18 22:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('favs', models.ManyToManyField(related_name='faved_books', to='main.User')),
            ],
        ),
    ]
