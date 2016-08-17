# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('datetime_attended', models.DateTimeField(default=datetime.datetime.now, verbose_name='Date Attended')),
                ('leaving', models.BooleanField(default=False, verbose_name='Currently looking to be subbed out')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('text', models.CharField(max_length=8000)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('date', models.DateField(verbose_name='Date of Event')),
                ('time', models.CharField(max_length=1000)),
                ('place', models.CharField(max_length=1000)),
                ('desc', models.CharField(verbose_name='Description', max_length=10000, null=True)),
                ('min_attendees', models.IntegerField(default=0, verbose_name='Minimum number of attendees')),
                ('max_attendees', models.IntegerField(default=9999, verbose_name='Maximum number of attendees')),
                ('lock_date', models.DateField(default=datetime.date.today, verbose_name='Date upon which people cannot leave the event if the minimum number of attendees has not been exceeded')),
                ('eventId', models.CharField(editable=False, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('image', models.ImageField(upload_to='events/images/')),
                ('caption', models.CharField(blank=True, max_length=2000)),
                ('event', models.ForeignKey(to='events.Event')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='event',
            field=models.ForeignKey(to='events.Event'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='attendee',
            name='event',
            field=models.ForeignKey(to='events.Event', related_name='signed_up'),
        ),
        migrations.AddField(
            model_name='attendee',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
