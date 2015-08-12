from django.shortcuts import *
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

# Create your views here.
def index(request):
    context = {"title" : "Events - Home", "content" : "placeholder"}
    return render(request, 'base.html', context)