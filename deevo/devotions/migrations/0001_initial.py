# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-09 15:50
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
            name='Devotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('verse_start', models.IntegerField()),
                ('verse_end', models.IntegerField()),
                ('version_id', models.IntegerField()),
                ('reflection', models.TextField()),
                ('pub_date', models.DateTimeField()),
                ('edit_date', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]