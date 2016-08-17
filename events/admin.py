from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *
from django.contrib.auth.models import User


# Register your models here.
class NiceUserInline(admin.TabularInline):
    """
    In addition to showing a user's username in related fields, show their full
    name too (if they have one and it differs from the username).
    """
    extra = 0
    always_show_username = True

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        field = super(NiceUserInline, self).formfield_for_foreignkey(
                                                db_field, request, **kwargs)
        if db_field.rel.to == User:
            field.label_from_instance = self.get_user_label
        return field

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        field = super(NiceUserModelAdmin, self).formfield_for_manytomany(
                                                db_field, request, **kwargs)
        if db_field.rel.to == User:
            field.label_from_instance = self.get_user_label
        return field

    def get_user_label(self, user):
        name = user.get_full_name()
        username = user.username
        if not self.always_show_username:
            return name or username
        return (name and name != username and '%s (%s)' % (name, username)
                or username)

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    
    
class ImageInline(admin.TabularInline):
    model = Image
    extra = 0

class AttendeeInline(NiceUserInline):
    model = Attendee
    extra = 0

class CaptainInline(NiceUserInline):
    model = Captain
    extra = 0

class EventAdmin(admin.ModelAdmin):
    inlines = [CaptainInline, AttendeeInline, CommentInline, ImageInline]
    

admin.site.register(Event, EventAdmin)

#admin.site.register(GalleryImage)