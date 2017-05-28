# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-27 08:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20170526_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friends',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Friends_Status', to_field='code'),
        ),
        migrations.AlterField(
            model_name='friends_status',
            name='code',
            field=models.CharField(max_length=3, unique=True),
        ),
        migrations.AlterField(
            model_name='friends_status',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=11, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]