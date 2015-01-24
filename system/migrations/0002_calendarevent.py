# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalendarEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name='Title', blank=True)),
                ('start', models.DateTimeField(verbose_name='Start')),
                ('end', models.DateTimeField(verbose_name='End')),
                ('all_day', models.BooleanField(default=False, verbose_name='All day')),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
            bases=(models.Model,),
        ),
    ]
