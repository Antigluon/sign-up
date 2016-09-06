from social.apps.django_app.middleware import SocialAuthExceptionMiddleware
from django.http import HttpResponseRedirect
from social import exceptions as social_exceptions 
from django.core.urlresolvers import reverse

class AuthExceptionMiddleware(SocialAuthExceptionMiddleware):
    def process_exception(self, request, exception):
        if hasattr(social_exceptions, exception.__class__.__name__):
            return HttpResponseRedirect(reverse("events:loginerror"))
        else:
            raise exception