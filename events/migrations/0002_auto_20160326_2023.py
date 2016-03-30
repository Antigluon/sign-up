# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='lock_date',
            field=models.DateField(verbose_name='Date upon which people cannot leave the event if the minimum number of attendees has not been exceeded', default=datetime.date(2016, 3, 26)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='max_attendees',
            field=models.IntegerField(verbose_name='Maximum number of attendees', default=9999),
        ),
        migrations.AddField(
            model_name='event',
            name='min_attendees',
            field=models.IntegerField(verbose_name='Minimum number of attendees', default=0),
        ),
        migrations.AddField(
            model_name='event',
            name='sub_waitlist',
            field=models.ManyToManyField(related_name='substitutes', db_constraint='People wanting to be substituted in if somebody leaves the event', blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
