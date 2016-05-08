# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_auto_20160504_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendee',
            name='datetime_attended',
            field=models.DateTimeField(verbose_name='Date Attended', default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='leaving',
            field=models.BooleanField(verbose_name='Currently looking to be subbed out', default=False),
        ),
    ]
