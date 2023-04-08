from django.apps import AppConfig


class DataparserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dataParser'

    def ready(self):
        from . import signals