from django.apps import AppConfig


class EventsConfig(AppConfig):

    name = 'events'
    verbose_name = 'Events'

    def ready(self):
        import events.signals