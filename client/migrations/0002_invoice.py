# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0001_initial'),
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=20)),
                ('issueDate', models.DateField(null=True, blank=True)),
                ('employee', models.ForeignKey(to='hr.Employee')),
                ('payments', models.ManyToManyField(to='client.Payment')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
