from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
import datetime

class Event(models.Model):
    name = models.CharField(max_length = 255)
    date = models.DateField("Date of Event")
    time = models.CharField(max_length = 1000)
    place = models.CharField(max_length = 1000)
    desc = models.CharField("Description", max_length = 10000, null = True)
    min_attendees = models.IntegerField("Minimum number of attendees", default=0)
    max_attendees = models.IntegerField("Maximum number of attendees", default=9999)
    lock_date = models.DateField("Date upon which people cannot leave the event if the minimum number of attendees has not been exceeded", default=datetime.date.today)
    eventId = models.CharField(max_length=200,editable=False)
    
    def locked(self):
        if self.lock_date >= datetime.date.today():
            return True
        else:
            return False
    
    def viewable(self):
        return True
        
    def users(self):
        return [attendee.user for attendee in self.signed_up.all()]
        
    def attending(self):
        if len(self.users()) >= self.max_attendees:
            numToPick = self.max_attendees
            return [attendee.user for attendee in self.signed_up.all().order_by('datetime_attended')[:numToPick]]
        else:
            return self.users()
    
    def leaving(self):
        leaving = []
        for attendee in self.signed_up():
            if attendee.leaving:
                leaving.append(attendee.user)
        return leaving
        
    def __str__(self):
        return str(self.name)
        
class Comment(models.Model):
    user = models.ForeignKey(User)
    text  = models.CharField(max_length = 8000)
    event = models.ForeignKey(Event)
    def __str__(self):
        return str(self.text)
    
class Image(models.Model):
    image = models.ImageField(upload_to="events/images/")
    caption = models.CharField(max_length=2000,blank=True)
    event = models.ForeignKey(Event)
    
class Attendee(models.Model):
    user = models.ForeignKey(User)
    event = models.ForeignKey(Event, related_name="signed_up")
    datetime_attended  = models.DateTimeField("Date Attended", default=datetime.datetime.now)
    leaving = models.BooleanField("Currently looking to be subbed out", default=False)
    
    def __str__(self):
        return str(self.user)
    
    
    