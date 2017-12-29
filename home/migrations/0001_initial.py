# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-28 09:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'categorys',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('organizer', models.CharField(default='', max_length=256)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('slug', models.SlugField(default='')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Category')),
            ],
            options={
                'db_table': 'events',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('street', models.CharField(default='', max_length=30)),
                ('city', models.CharField(default='', max_length=30)),
                ('country', models.CharField(default='', max_length=30)),
            ],
            options={
                'db_table': 'locations',
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='events',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Location'),
        ),
    ]
