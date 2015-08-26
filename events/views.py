from django.shortcuts import *
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from .models import *

def index(request):
    context = {"events_" : Event.objects.all()}
    return render(request, 'home.html', context)
    

