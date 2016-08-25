from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from copy import deepcopy

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
class SafeUserAdmin(UserAdmin):

    def get_fieldsets(self, request, obj=None):
        fieldsets = super(UserAdmin, self).get_fieldsets(request, obj)
        if not obj:
            return fieldsets

        if not request.user.is_superuser or request.user.pk == obj.pk:
            fieldsets = deepcopy(fieldsets)
            for fieldset in fieldsets:
                if 'is_superuser' in fieldset[1]['fields']:
                    if type(fieldset[1]['fields']) == tuple :
                        fieldset[1]['fields'] = list(fieldset[1]['fields'])
                    fieldset[1]['fields'].remove('is_superuser')
                    if not request.user.is_superuser:
                        fieldset[1]['fields'].remove('user_permissions')
                    break

        return fieldsets
#admin.site.register(GalleryImage)
admin.site.unregister(User)
admin.site.register(User, SafeUserAdmin)