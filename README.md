## DRF playground

### Requirements that is not included in requirements.txt
- ms sql server driver 17 - download in microsoft site, driver only works in windows, so can't be developed in other OS rather than windows?
- ms sql server can be executed easily via docker, no needed to fill forms of trial days.

#### example of dotenv (.env) file

```
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
```


#### install the requirements every time when the code is pulled from github to avoid some problems

```
pip installl -r requirements.txt
```

#### after that run migrate

```
python manage.py migrate
```

#### and run django

```
python manage.py runserver
```
