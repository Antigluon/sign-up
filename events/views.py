from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

# Create your views here.
def index(request):
    return HttpResponse("You're looking at question?")