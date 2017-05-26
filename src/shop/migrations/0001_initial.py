# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-25 16:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_name', models.CharField(max_length=50)),
                ('price', models.IntegerField(verbose_name=10)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('img', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('description', models.TextField(blank=True)),
                ('shop_phone1', models.CharField(blank=True, max_length=13)),
                ('shop_phone2', models.CharField(blank=True, max_length=13)),
                ('is_available', models.BooleanField(default=1)),
                ('img', models.CharField(blank=True, max_length=255, null=True)),
                ('thumbnail', models.CharField(blank=True, max_length=255, null=True)),
                ('open', models.SmallIntegerField()),
                ('close', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Shop_Apply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('regi_num', models.CharField(blank=True, max_length=30, unique=True)),
                ('category', models.CharField(max_length=20)),
                ('applied', models.DateTimeField()),
                ('approved', models.DateTimeField(null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='shop',
            name='apply_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Shop_Apply'),
        ),
        migrations.AddField(
            model_name='shop',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='menu',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Shop'),
        ),
        migrations.AlterUniqueTogether(
            name='menu',
            unique_together=set([('menu_name', 'shop')]),
        ),
    ]
