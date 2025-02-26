import os

# Configuración de Django
os.environ["DJANGO_SETTINGS_MODULE"] = "session.settings"

# No es necesario definir estas variables aquí si ya están en tu .env
# Django leerá automáticamente el archivo .env si usas django-environ
# o python-dotenv en tu settings.py
#
# Asegúrate de que tu aplicación cargue el archivo .env en settings.py
# Por ejemplo, usando:
# import environ
# env = environ.Env()
# environ.Env.read_env()

# Configuración de la aplicación WSGI
wsgi_app = "session.wsgi:application"

# Configuración del servidor
debug = False
bind = "0.0.0.0:8000"  # Escucha en todas las interfaces
workers = 2
worker_connections = 250
max_requests = 500
max_requests_jitter = 500
graceful_timeout = 120
timeout = 120
keepalive = 5

# Configuración de logs - descomenta y configura según necesites
# errorlog = "/var/log/djangoplayground/gunicorn-error.log"
# loglevel = "info"
# accesslog = "/var/log/djangoplayground/gunicorn-access.log"
# access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
