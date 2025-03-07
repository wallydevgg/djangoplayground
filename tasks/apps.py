import warnings
from django.apps import AppConfig


class TasksConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "tasks"

    def ready(self):
        # se coloco el warining para ignrar los warnings de runtime y relizar las migraciones en DB
        warnings.filterwarnings("ignore", category=RuntimeWarning)

        # Check if we're running migrations to avoid the chicken-and-egg problem
        import sys

        if "migrate" in sys.argv or "makemigrations" in sys.argv:
            return  # Skip scheduler initialization during migrations

        from .scheduler import initialize

        initialize()
