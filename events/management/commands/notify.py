from django.core.management.base import BaseCommand, CommandError
from events.models import *
from django.core.mail import send_mail
import datetime
from django.utils import formats


class Command(BaseCommand):
    help = 'Checks if any events will occur today and sends email notifications for them.'

    def handle(self, *args, **options):
        for event in Event.objects.all().filter(date=datetime.date.today()):
            emails=[]
            for user in event.signed_up.all():
                emails.append(user.email)
            message = """ {0} is on {1}{4}at {2} at {3}. You are signed up, so remember to attend!
            """.format(event.name, formats.date_format(event.date), event.time, event.place, ' (that\'s today) ' if event.date==datetime.date.today() else ' ')
            send_mail(event.name + ' is today!', message, 'no-reply@okemosaction.net', emails)
            self.stdout.write(event.name)