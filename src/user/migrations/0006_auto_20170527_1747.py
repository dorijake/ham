# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-27 08:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20170527_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friends',
            name='friend',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_list', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='friends',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_list', to=settings.AUTH_USER_MODEL),
        ),
    ]