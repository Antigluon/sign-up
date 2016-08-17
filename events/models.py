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
    min_attendees = models.IntegerField("Minimum number of attendees (not including captain[s])", default=0)
    max_attendees = models.IntegerField("Maximum number of attendees (not including captain[s])", default=9999)
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
            users = [attendee for attendee in (self.signed_up.all().order_by('datetime_attended')[:numToPick])]
            return [attendee.user for attendee in users if not attendee.missed]
        else:
            return self.users()
    
    def captain_list(self):
        return [captain.user for captain in self.captains.all()]
        
    def leaving(self):
        leavings = []
        for attendee in self.signed_up.all():
            if attendee.leaving:
                leavings.append(attendee.user)
        return leavings
    
    def missed(self):
        missing = []
        for attendee in self.signed_up.all():
            if attendee.missed:
                missing.append(attendee.user)
        return missing
    
    def disp_captains(self):
        sequence = self.captains.all()
        if not sequence:
            return 'Nobody'
        if len(sequence) == 1:
            return sequence[0]
        return '{} and {}'.format(', '.join(map(str,sequence[:len(sequence)-1])), str(sequence[len(sequence)-1]))

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
    
class GalleryImage(models.Model):
    image = models.ImageField(upload_to="events/images/")
    caption = models.CharField(max_length=2000,blank=True)
    def __str__(self):
        return str(self.caption)
    
class Attendee(models.Model):
    user = models.ForeignKey(User)
    event = models.ForeignKey(Event, related_name="signed_up")
    datetime_attended  = models.DateTimeField("Date Attended", default=datetime.datetime.now)
    leaving = models.BooleanField("Currently looking to be subbed out", default=False)
    missed = models.BooleanField("Did not come to event", default=False)
    
    def __str__(self):
        return self.user.get_full_name()
    
class Captain(models.Model):
    user = models.ForeignKey(User, limit_choices_to={'groups__name__in': ["Captains", "Admins"]})
    event = models.ForeignKey(Event, related_name="captains")
    def __str__(self):
        return self.user.get_full_name()
    