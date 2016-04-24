# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20160404_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='eventId',
            field=models.CharField(editable=False, max_length=200, default=0),
            preserve_default=False,
        ),
    ]
