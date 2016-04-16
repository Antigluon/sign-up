from apiclient.discovery import build
from settings.py import *
class Calendar:
    service = build('calendar', 'v3', developerKey = CALENDAR_API_KEY)
    def __init__(self):
        pass
    
    
