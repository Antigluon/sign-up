# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Date of Event')),
                ('place', models.CharField(max_length=1000)),
                ('name', models.CharField(max_length=255)),
                ('pub_date', models.DateTimeField(verbose_name='Date when people can sign up')),
                ('signed_up', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
