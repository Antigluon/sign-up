from django.conf.urls import url

from events import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^attendEvent/$', views.attendEvent, name="attendEvent"),
    url(r'^leaveEvent/$', views.leaveEvent, name="leaveEvent"),
    url(r'^unQueueLeave/$', views.unQueueLeave, name="unQueueLeave"),
    url(r'^photos/$', views.photos, name="photos")
] 
