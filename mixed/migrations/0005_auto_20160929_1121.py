# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-29 11:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mixed', '0004_auto_20160928_1549'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomConverter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('context', models.TextField()),
                ('output_type', models.CharField(choices=[('F', 'Function'), ('S', 'String')], default='F', max_length=1)),
                ('output', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='document',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='document',
            name='custom_converter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mixed.CustomConverter'),
        ),
    ]
