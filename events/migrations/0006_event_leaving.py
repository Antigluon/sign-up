# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0005_event_eventid'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='leaving',
            field=models.ManyToManyField(related_name='leaving', blank=True, to=settings.AUTH_USER_MODEL, editable=False),
        ),
    ]
