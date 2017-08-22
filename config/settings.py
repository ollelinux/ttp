from .base import *

DEBUG = True

SECRET_KEY = 'Any_set_of_symbols'

ALLOWED_HOSTS += ['127.0.0.1', 'localhost',]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ttp',
        'USER': 'ttpuser',
        'PASSWORD': 'us3rtt9',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


INSTALLED_APPS += ['debug_toolbar', ]
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

