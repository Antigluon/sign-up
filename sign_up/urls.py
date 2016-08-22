from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url('', include('events.urls', namespace = "events")),
    #url('^register/', views.register, name = 'register'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
