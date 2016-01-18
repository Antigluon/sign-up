# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20160118_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='desc',
            field=models.CharField(null=True, verbose_name='Description', max_length=10000),
        ),
    ]
