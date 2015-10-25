from django import forms
from .forms import UserCreateForm
from django.http import HttpResponseRedirect
from django.shortcuts import render

def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = UserCreateForm()
    return render(request, "registration/register.html", {
        'form': form,
    })