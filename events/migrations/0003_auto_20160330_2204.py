# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20160326_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='lock_date',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Date upon which people cannot leave the event if the minimum number of attendees has not been exceeded'),
        ),
    ]
