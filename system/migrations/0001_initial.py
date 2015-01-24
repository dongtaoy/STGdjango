# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Icon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('css', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('css', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sidebar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=45, blank=True)),
                ('url', models.CharField(max_length=100, blank=True)),
                ('order', models.IntegerField(max_length=10, null=True, blank=True)),
                ('icon', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='system.Icon', null=True)),
                ('parent', models.ForeignKey(related_name='children', blank=True, to='system.Sidebar', null=True)),
            ],
            options={
                'ordering': ['order'],
            },
            bases=(models.Model,),
        ),
    ]
