"""
WSGI config for session project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
from dotenv import read_dotenv

from django.core.wsgi import get_wsgi_application

read_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'session.settings')

application = get_wsgi_application()
