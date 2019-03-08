DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': 'test.db',
    },
    'loggers': {
        '': {
            # this sets root level logger to log debug and higher level
            # logs to console. All other loggers inherit settings from
            # root level logger.
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False, # this tells logger to send logging message
                                # to its parent (will send if set to True)
        },
        'django.db': {
            'level': 'DEBUG',
            # django also has database level logging
        }
    }
}

INSTALLED_APPS = (
    'data',
    )

SECRET_KEY = 'REPLACE_ME'