# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=b'50', null=True, blank=True)),
                ('css', models.CharField(max_length=b'50', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
