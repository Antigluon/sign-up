from django.conf.urls import patterns, url

from events import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^attendEvent/$', views.attendEvent, name="attendEvent"),
    url(r'^leaveEvent/$', views.leaveEvent, name="leaveEvent")
)
