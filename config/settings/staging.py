from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ticket_office_local',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
