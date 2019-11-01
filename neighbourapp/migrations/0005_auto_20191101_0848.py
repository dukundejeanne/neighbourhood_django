# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-01 08:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('neighbourapp', '0004_auto_20191031_1322'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=40)),
                ('bussiness_email', models.EmailField(max_length=200, null=True)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('bussiness', models.CharField(max_length=200)),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='neighbourapp.Neighbour')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=100)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neighbourapp.Neighbour')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='posted_by',
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
