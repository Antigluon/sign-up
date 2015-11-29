# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='caption',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='events/images/'),
        ),
    ]
