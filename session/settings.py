"""
Django settings for session project.

Generated by 'django-admin startproject' using Django 5.0.12.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from os import environ
from pathlib import Path
from datetime import timedelta


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(environ.get("DEBUG"))

ALLOWED_HOSTS = environ.get("ALLOWED_HOSTS", "").split(",")

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework_simplejwt",
    "drf_yasg",
    "users",
    "authentication",
    "balanza",
    "category",
    "products",
    "shopping_cart",
    "coupons",
    "tasks",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "session.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "session.wsgi.application"

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": environ.get("DB_ENGINE"),
        "NAME": environ.get("DB_NAME"),
        "USER": environ.get("DB_USER"),
        "PASSWORD": environ.get("DB_PASSWORD"),
        "HOST": environ.get("DB_HOST"),
        "PORT": environ.get("DB_PORT"),
        "OPTIONS": {
            "driver": environ.get("DB_DRIVER"),
        },
    },
}

TIME_ZONE = environ.get("TIMEZONE")

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# modelo de usuario personalizado

AUTH_USER_MODEL = "users.User"

# configuracion swagger
# https://drf-yasg.readthedocs.io/en/stable/settings.html
SWAGGER_SETTINGS = {
    # https://drf-yasg.readthedocs.io/en/stable/settings.html#security-definitions
    "SECURITY_DEFINITIONS": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
        }
    },
    # deshabilitacion la opciopn autentiacion de django en el swagger
    "USE_SESSION_AUTH": False,
}

# Configuracion de JWT
# https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),  # produccion 5min, dev 30min
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "SIGNING_KEY": environ.get("SECRET_KEY"),
}

# configuracion de DRF
# https://www.django-rest-framework.org/api-guide/settings/
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PAGINATION_CLASS": "session.core.pagination.CustomPagination",
}


# configurar el correo
# https://docs.djangoproject.com/en/5.1/topics/email/
EMAIL_BACKEND = environ.get("MAIL_BACKEND")
EMAIL_HOST = environ.get("MAIL_SERVER")
EMAIL_PORT = environ.get("MAIL_PORT")
EMAIL_USE_TLS = environ.get("MAIL_USE_TLS")
EMAIL_HOST_USER = environ.get("MAIL_USERNAME")
EMAIL_HOST_PASSWORD = environ.get("MAIL_PASSWORD")
# EMAIL_USE_SSL = environ.get("MAIL_USE_SSL")


# Configuracion de AWS
AWS_REGION = environ.get("AWS_REGION")
AWS_ACCESS_ID = environ.get("AWS_ACCESS_ID")
AWS_ACCESS_SECRET_KEY = environ.get("AWS_ACCESS_SECRET_KEY")
AWS_S3_BUCKET_NAME = environ.get("AWS_S3_BUCKET_NAME")
