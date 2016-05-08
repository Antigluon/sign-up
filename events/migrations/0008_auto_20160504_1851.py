# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_attendee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='leaving',
        ),
        migrations.RemoveField(
            model_name='event',
            name='signed_up',
        ),
        migrations.RemoveField(
            model_name='event',
            name='sub_waitlist',
        ),
        migrations.AlterField(
            model_name='attendee',
            name='datetime_attended',
            field=models.DateTimeField(verbose_name="You shouldn't be seeing this", default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='event',
            field=models.ForeignKey(to='events.Event', related_name='signed_up'),
        ),
    ]
