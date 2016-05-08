from django.shortcuts import *
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from .models import *
from django.contrib.auth.models import User
import random
from django.db.models import Count
import datetime
from django.core.mail import send_mail
from django.utils import formats


class Counter:
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
        return""
        
    def decrement(self):
        self.count -= 1
        
    def zero(self):
        self.count = 0
        return ""
        
    def get_count(self):
        return self.count
        
def getContext(context={}):
    context['events_'] = Event.objects.all
    context['users'] = User.objects.annotate(count=Count('attendee')).order_by('-count')
    context['counter'] = Counter()
    context['date'] = datetime.date.today()
    return context

def index(request):
    return render(request, 'home.html', getContext())

class DetailView(generic.DetailView):
    model = Event
    template_name = "events/detail.html"
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(DetailView, self).get_context_data(**kwargs)
        context = getContext(context)
        return context

def attendEvent(request):
    eventID = request.POST['event_']
    userID = request.POST['user']
    event = Event.objects.get(pk=eventID)
    user = User.objects.get(pk=userID)
    info = request.POST['info']
    if datetime.date.today() < event.date:
        a = Attendee(event=event,user=user)
        event.signed_up.add(a)
        thoseLeaving = event.signed_up.filter(leaving=True).order_by('datetime_attended')
        if len(event.users()) > event.min_attendees and thoseLeaving:
            thoseLeaving[0].delete()
            send_mail("You are no longer attending " + event.name, "Enough people have joined the event " + event.name
             + " that you no longer must attend. You have been removed from the event because you were queued to leave.", 
             'no-reply@okemosaction.net', [thoseLeaving[0].user.email])
        if info and not info.isspace():
            c = Comment(user=user,event=event,text=(info))
            c.save()
        event.save()
        #print(eventID)
    return HttpResponseRedirect(reverse("events:detail",kwargs={"pk":eventID}))
    
def leaveEvent(request):
    eventID = request.POST['event_']
    userID = request.POST['user']
    event = Event.objects.get(pk=eventID)
    user = User.objects.get(pk=userID)
    attendee = event.signed_up.get(user=user)
    if datetime.date.today() < event.date:
        if (len(event.users()) <= event.min_attendees) and event.locked():
            attendee.leaving = True
            attendee.save()
        else:
            attendee.delete()
        event.save()
        if len(event.users()) >= event.max_attendees:
            user = event.attending()[-1]
            send_mail("You are now attending " + event.name, "Somebody has dropped out of the event "\
            + event.name + ", so you are now one of the people attending said event. It is on " + formats.date_format(event.date) + ". Have fun!",
            'no-reply@okemosaction.net', [user.email])
    return HttpResponseRedirect(reverse("events:index"))
    
def unQueueLeave(request):
    eventID = request.POST['event_']
    userID = request.POST['user']
    event = Event.objects.get(pk=eventID)
    user = User.objects.get(pk=userID)
    attendee = event.signed_up.get(user=user)
    if attendee.leaving:
        attendee.leaving = False
    return HttpResponseRedirect(reverse("events:index"))

def subwaySandwiches(request):
    #Too much sand witch error initiated
    print("Too many subs")
    return HttpResponseRedirect("https://www.subway.com")