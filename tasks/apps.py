import warnings
from django.apps import AppConfig


class TasksConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "tasks"

    def ready(self):
        # se coloco el warining para ignrar los warnings de runtime y relizar las migraciones en DB
        warnings.filterwarnings("ignore", category=RuntimeWarning)
        from .scheduler import initialize
        initialize()