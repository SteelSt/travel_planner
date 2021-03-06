# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-23 20:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('created_by', models.IntegerField()),
                ('dateto', models.DateField()),
                ('datefrom', models.DateField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='trip',
            name='all_users',
            field=models.ManyToManyField(related_name='all_trips', to='python_belt_exam_app.User'),
        ),
        migrations.AddField(
            model_name='trip',
            name='trip_users',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_trips', to='python_belt_exam_app.User'),
        ),
    ]
