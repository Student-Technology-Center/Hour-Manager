# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-28 02:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hour_manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='hour_history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover_first', models.CharField(max_length=15)),
                ('cover_last', models.CharField(max_length=20)),
                ('coveree_first', models.CharField(max_length=15)),
                ('coveree_last', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='hourmodel',
            name='end_time',
            field=models.TimeField(help_text='In military time.'),
        ),
        migrations.AlterField(
            model_name='hourmodel',
            name='reason',
            field=models.CharField(help_text='The reason you need this shift covered.', max_length=120),
        ),
        migrations.AlterField(
            model_name='hourmodel',
            name='start_time',
            field=models.TimeField(help_text='In military time.'),
        ),
    ]
