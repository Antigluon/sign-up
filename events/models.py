from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Event(models.Model):
    date = models.DateField("Date of Event")
    time = models.CharField(max_length = 1000)
    place = models.CharField(max_length = 1000)
    name = models.CharField(max_length = 255)
    desc = models.CharField("Description", max_length = 10000, null = True)
    pub_date = models.DateTimeField("Date when people can sign up")
    signed_up = models.ManyToManyField(User, blank = True)
    
    def viewable(self):
        return now() >= self.pub_date

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
    
    
    