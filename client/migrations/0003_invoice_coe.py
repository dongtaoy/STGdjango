# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_invoice'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='coe',
            field=models.ForeignKey(related_name='invoices', blank=True, to='client.Coe', null=True),
            preserve_default=True,
        ),
    ]
