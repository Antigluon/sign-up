from django.core.management.base import BaseCommand, CommandError
from events.models import *
from django.utils import formats
from django.contrib.auth.models import User, Group
import os

emailFile = open("events/management/commands/rawEmails.txt")
rawEmails = emailFile.read()
captainEmails = rawEmails.split(' ')
#print(captainEmails)
emailFile.close()

class Command(BaseCommand):
    help = 'Adds everyone with an email belonging to a captain to the Captains group and marks them as staff.'

    def handle(self, *args, **options):
        captains = User.objects.filter(email__in=captainEmails)
        captains.update(is_staff=True)
        updated = []
        for captain in captains:
            if not captain.groups.filter(name="Captains").exists():
                updated.append(captain)
            captain.groups.add(Group.objects.get(name="Captains"))
            captain.save()
        #print(captains) 
        