# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20160330_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='signed_up',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True, related_name='signed_up'),
        ),
    ]
