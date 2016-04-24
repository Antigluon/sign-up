from __future__ import print_function
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.conf import settings
from .models import Event
from apiclient.discovery import build
from sign_up.settings import *
import os.path
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from oauth2client.service_account import ServiceAccountCredentials

def get_cal():
    scopes = ['https://www.googleapis.com/auth/calendar']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('/home/ubuntu/workspace/Okemos Action-7e118ff1217e.json', scopes)
    #credentials = ServiceAccountCredentials.from_json(os.environ['GOOGLE_API']).create_scoped(scopes)
    http_auth = credentials.authorize(Http())
    CAL = build('calendar', 'v3', http=http_auth)
    return CAL

@receiver(post_save, sender=Event)
def model_post_save(sender, **kwargs):
    CAL = get_cal()
    event = kwargs['instance']
    start_end = str(event.date)
    EVENT = {
        'summary': event.name,
        'start':  {'date': start_end},
        'end':    {'date': start_end},
        'description': event.desc,
        'guestsCanInviteOthers': False,
    }
    attendees = []
    for user in event.signed_up.all():
        attendees.append({'email': user.email})
    EVENT['attendees'] = attendees
    if kwargs['created']:
        e = CAL.events().insert(calendarId=os.environ['CALENDAR_ID'],
                sendNotifications=True, body=EVENT).execute()
        event.eventId = e['id']
        event.save()
    else:
        CAL.events().update(calendarId=os.environ['CALENDAR_ID'], eventId=event.eventId,
                sendNotifications=True, body=EVENT).execute()
                
@receiver(pre_delete, sender=Event)
def model_pre_delete(sender, **kwargs):
    CAL = get_cal()
    event = kwargs['instance']
    CAL.events().delete(calendarId=os.environ['CALENDAR_ID'], eventId=event.eventId,
                sendNotifications=True).execute()
    