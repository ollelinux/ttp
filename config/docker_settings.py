from .base import *

DEBUG = True

SECRET_KEY = 'Any_set_of_symbols'

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASS'),
        'HOST': os.environ.get('DB_SERVICE'),
        'PORT': os.environ.get('DB_PORT'), 
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

