# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-16 08:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0003_auto_20161009_0326'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, null=True, verbose_name='第一志愿')),
                ('description', models.TextField(blank=True, null=True, verbose_name='第一志愿')),
            ],
            options={
                'verbose_name_plural': '管理层第一志愿报名',
                'verbose_name': '管理层第一志愿报名',
            },
        ),
        migrations.CreateModel(
            name='Group2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, null=True, verbose_name='第二志愿')),
                ('description', models.TextField(blank=True, null=True, verbose_name='第二志愿')),
            ],
            options={
                'verbose_name_plural': '管理层第二志愿报名',
                'verbose_name': '管理层第二志愿报名',
            },
        ),
        migrations.RemoveField(
            model_name='newmember',
            name='group',
        ),
        migrations.AlterField(
            model_name='newmember',
            name='email',
            field=models.CharField(max_length=64, verbose_name='qq或微信'),
        ),
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.AddField(
            model_name='newmember',
            name='group1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='welcome.Group1', verbose_name='第一志愿'),
        ),
        migrations.AddField(
            model_name='newmember',
            name='group2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='welcome.Group2', verbose_name='第二志愿'),
        ),
    ]
