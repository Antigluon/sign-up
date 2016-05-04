from django.shortcuts import *
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from .models import *
from django.contrib.auth.models import User
import random
from django.db.models import Count

def getContext(context={}):
    context['events_'] = Event.objects.all
    context['users'] = User.objects.all().annotate(count=Count('signed_up')).order_by('-count')
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
    if event.leaving.count() > 0:
        replaced = event.leaving.all()[0]
        event.leaving.remove(replaced)
        event.signed_up.remove(replaced)
        event.save()
        c = Comment(user=user,event=event,text=(info+' '))
        c.save()
    elif event.signed_up.count() < event.max_attendees:
        info = request.POST['info']
        event.signed_up.add(user)
        c = Comment(user=user,event=event,text=(info+' '))
        c.save()
    else:
        event.substitutes.add(user)
    event.save()
    #print(eventID)
    return HttpResponseRedirect(reverse("events:detail",kwargs={"pk":eventID}))
    
def leaveEvent(request):
    eventID = request.POST['event_']
    userID = request.POST['user']
    event = Event.objects.get(pk=eventID)
    user = User.objects.get(pk=userID)
    if user in event.signed_up.all():
        event.signed_up.remove(user)
    elif user in event.substitutes.all():
        event.substitutes.remove(user)
    event.save()
    return HttpResponseRedirect(reverse("events:index"))
    
def addSub(request):
    eventID = request.POST['event_']
    userID = request.POST['user']
    event = Event.objects.get(pk=eventID)
    user = User.objects.get(pk=userID)
    event.substitutes.add(user)
    event.save()
    return HttpResponseRedirect(reverse("events:detail",kwargs={"pk":eventID}))

def wantSub(request):
    eventID = request.POST['event_']
    userID = request.POST['user']
    event = Event.objects.get(pk=eventID)
    user = User.objects.get(pk=userID)
    event.leaving.add(user)
    event.save()
    return HttpResponseRedirect(reverse("events:index"))
    
def subwaySandwiches(request):
    #Too much lol error initiated
    print("Too many subs")
    return HttpResponseRedirect("https://www.subway.com")