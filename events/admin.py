from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *

# Register your models here.

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class EventAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    

admin.site.register(Event, EventAdmin)
#admin.site.register(Comment)
#admin.site.unregister(Group)