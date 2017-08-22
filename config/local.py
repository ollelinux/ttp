from .base import *

DEBUG = True

SECRET_KEY = 'Any_set_of_symbols'
# SECRET_KEY = ')2!vvhn6wuj_fkz!ljg#%hgcs5tw8s4eg^(8h37w$^%=7%@sd%'

ALLOWED_HOSTS += ['127.0.0.1', 'localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ttp',
        'USER': 'ttpuser',
        'PASSWORD': 'us3rtt9',
        'HOST': 'localhost'
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


INSTALLED_APPS += ['debug_toolbar', ]
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]
