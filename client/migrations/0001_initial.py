# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import client.models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '__first__'),
        ('hr', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('preferredName', models.CharField(max_length=100, null=True, blank=True)),
                ('dob', models.DateField(null=True, blank=True)),
                ('nationality', models.CharField(max_length=100, null=True, blank=True)),
                ('email', models.EmailField(max_length=75, null=True, blank=True)),
                ('phone', models.CharField(max_length=20, null=True, blank=True)),
                ('onshore', models.BooleanField(default=True)),
                ('expire', models.DateField(null=True, blank=True)),
                ('status', models.CharField(default=b'Ongoing', max_length=10, null=True, blank=True, choices=[(b'Ongoing', b'Ongoing'), (b'Existing', b'Existing'), (b'Close', b'Close')])),
                ('serviceFee', models.FloatField(null=True, blank=True)),
                ('thirdPartyFeeReceived', models.FloatField(null=True, blank=True)),
                ('thirdPartyFeePaid', models.FloatField(null=True, blank=True)),
                ('note', models.TextField(null=True, blank=True)),
                ('clientManager', models.ForeignKey(related_name='cm', blank=True, to='hr.Employee', null=True)),
                ('consultant', models.ForeignKey(related_name='con', blank=True, to='hr.Employee', null=True)),
                ('referal', models.ForeignKey(related_name='ref', blank=True, to='hr.Employee', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Coe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('coeNumber', models.CharField(max_length=30, null=True, blank=True)),
                ('start', models.DateField(null=True, blank=True)),
                ('end', models.DateField(null=True, blank=True)),
                ('totalTuitionFee', models.FloatField(null=True, blank=True)),
                ('bonus', models.FloatField(null=True, blank=True)),
                ('referalCommission', models.FloatField(null=True, blank=True)),
                ('consultantCommission', models.FloatField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('client', models.ForeignKey(related_name='coes', to='client.Client')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, null=True, blank=True)),
                ('file', models.FileField(upload_to=client.models.rename_file)),
                ('coe', models.ForeignKey(related_name='files', to='client.Coe')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(null=True, blank=True)),
                ('label', models.ForeignKey(blank=True, to='system.Label', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('receivedAmount', models.FloatField(null=True, blank=True)),
                ('receivedDate', models.DateField(null=True, blank=True)),
                ('paidAmount', models.FloatField(null=True, blank=True)),
                ('paidDate', models.DateField(null=True, blank=True)),
                ('commssionClaimed', models.FloatField(null=True, blank=True)),
                ('commssionRecevied', models.FloatField(null=True, blank=True)),
                ('nextDueDate', models.DateField(null=True, blank=True)),
                ('coe', models.ForeignKey(related_name='payments', to='client.Coe')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.IntegerField(max_length=10)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ['order'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Visa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subClass', models.IntegerField(max_length=3)),
                ('description', models.TextField(max_length=100, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='document',
            name='stage',
            field=models.ForeignKey(to='client.Stage'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='coe',
            name='documents',
            field=models.ManyToManyField(to='client.Stage', null=True, through='client.Document', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='coe',
            name='institution',
            field=models.ForeignKey(blank=True, to='client.Institution', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='client',
            name='visa',
            field=models.ForeignKey(blank=True, to='client.Visa', null=True),
            preserve_default=True,
        ),
    ]
