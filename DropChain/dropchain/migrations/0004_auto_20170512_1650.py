# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-12 16:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dropchain', '0003_challenge_typechallenge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='challenge',
            name='description',
        ),
        migrations.RemoveField(
            model_name='challenge',
            name='name',
        ),
        migrations.AddField(
            model_name='challenge',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='typechallenge',
            name='description',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]