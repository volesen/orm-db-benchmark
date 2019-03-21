import dj_database_url

DATABASES ={}
DATABASES['default'] = dj_database_url.config(conn_max_age=600)

INSTALLED_APPS = (
    'data',
    )

SECRET_KEY = 'REPLACE_ME'