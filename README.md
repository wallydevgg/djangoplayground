## DRF playground

### Requirements that is not included in the dependencies (requirements.txt)

- [MS SQL Server Driver 17](https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver16) 
- [MS SQL Server Docker image](https://hub.docker.com/r/microsoft/mssql-server) can be executed easy to run, no needed to fill forms of trial days.

##### ~ dotenv (.env) file - included on this repo

### Install the requirements every time when the code is pulled from github to avoid some problems

```
pip installl -r requirements.txt

```

#### everytime we create or edit a model...

```
python manage.py makemigrations
```

#### and then...

#### after that run migrate

```
python manage.py migrate
```

-  if the tables doesnt appear in database, delete the corresponding row (row - name of app) in the table 'django_migrations' of the database. And then try again 'makemigrations' and 'migrations' again

#### and run django

```
python manage.py runserver
```
