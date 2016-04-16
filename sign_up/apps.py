from django.apps import AppConfig


class MyAppConfig(AppConfig):

    name = 'myapp'
    verbose_name = 'My App'

    def ready(self):

        # import signal handlers
        import sign_up.signals.handlersa