from django.shortcuts import *
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from .models import *
from django.contrib.auth.models import User

def index(request):
    context = {"events_" : Event.objects.filter(date__lte=timezone.now()).order_by('-pub_date')}
    return render(request, 'home.html', context)

class DetailView(generic.DetailView):
    model = Event
    template_name = "events/detail.html"

def attendEvent(request):
    info = request.POST['info']
    eventID = request.POST['event_']
    userID = request.POST['user']
    event = Event.objects.get(pk=eventID)
    user = User.objects.get(pk=userID)
    event.signed_up.add(user)
    event.save()
    c = Comment(user=user,event=event,text=info)
    c.save()
    #print(eventID)
    return HttpResponseRedirect(reverse("events:detail",kwargs={"pk":eventID}))
    
def leaveEvent(request):
    eventID = request.POST['event_']
    userID = request.POST['user']
    event = Event.objects.get(pk=eventID)
    user = User.objects.get(pk=userID)
    for comment in user.comment_set.all():
        if comment.event == event:
            comment.delete()
    event.signed_up.remove(user)
    return HttpResponseRedirect(reverse("events:index"))
    
     