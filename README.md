## DRF playground

#### Disclamer:

This readme is personal annotations for me, like an 'quick cheatsheet' of django and this project is a good example of a project with django and drf. Even the code itself if a good documentation of how to do things in django and drf.

### Requirements that are not included in the dependencies (requirements.txt)

- [MS SQL Server Driver 17](https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver16)
  - stable and easy on windows, linux and macOS could be a little bit tricky
- [MS SQL Server Docker image](https://hub.docker.com/r/microsoft/mssql-server), no needed to fill forms of trial days.
  - useful for docker lovers
  - easy to run

##### ~ dotenv (.env) file - included on this repo. You can changue to the values you want, but be sure no sync to ther values that are on the settings.py file.

### Noobie instrucions (if you wanna to it in a new project - ignore if your are a pro)

```python
create environment:

python -m venv venv
./venv/Scripts/activate - windows
source venv/bin/activate - linux/macOS
```

### Install the dependencies:

```
pip installl -r requirements.txt

```

## create and .env file on the root of the project:

```python
DEBUG=true

DB_ENGINE=mssql
DB_NAME=playground
DB_USER=sa
DB_PASSWORD="yourStrong#Password"
DB_HOST=localhost
DB_PORT=1433
DB_DRIVER='ODBC Driver 17 for SQL Server'

TIMEZONE='America/Lima'

SECRET_KEY='mondongo'

MAIL_SERVER='smtp.gmail.com'
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME='YOUREMAIL@gmail.com'
MAIL_PASSWORD='YOUR PASSWORD'

AWS_REGION='YOUR REGION'
AWS_ACCESS_ID='YOUR ACCESS ID'
AWS_ACCESS_SECRET_KEY='YOUR SECRET KEY'

```

### read dotenv on wsgi.py:

```python
#wsgi.py
from dotenv import read_dotenv
...
read_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))
```

### set the .env values on settings.py:

```python
from os import environ
...
DEBUG = bool(environ.get("DEBUG"))
...
#apps of the project, could be requirements too like drf yasg,etc
INSTALLED_APPS = [
  ...
    #exapmple:
    "rest_framework",
    "rest_framework_simplejwt",
    "drf_yasg",
    "** any app created with <django-admin startapp *appname*> **",
  ...
]
...
#setting of the JWT of the project
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "SIGNING_KEY": environ.get("SECRET_KEY"),
}
...
#setting the templates folder to the project
TEMPLATES = [
    {
        ...
        "DIRS": ["templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
            ...
            ],
        },
    },
]
...
#setting database according to the .env file
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
...
#timezone settings defined on the .env file
TIME_ZONE = environ.get("TIMEZONE")

# You can see more related config of settings.py on the file itself,
# including the link of related documentation of the external or internal library

# Happy coding!

```

#### everytime we create or edit a model...

```

python manage.py makemigrations

```

#### and then, after that run migrate

```
python manage.py migrate

```

- if the tables doesnt appear in database:
  - in database: delete the corresponding row (row - 'name of app') in the table 'django_migrations'.
  - And then try again 'makemigrations' and 'migrations' again. And related models(tables in db) should appear.

#### Run django

```

python manage.py runserver

```
