from django.apps import AppConfig


class CarConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'car'
    def ready(self):
        import car.signals
