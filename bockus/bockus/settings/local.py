import os

from .base import *

SECRET_KEY = os.environ["SECRET_KEY"]

DEBUG = True
TEMPLATE_DEBUG = DEBUG

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
	"default": {
		"ENGINE": "django.db.backends.postgresql_psycopg2",
		"NAME": "bcokus",
		"USER": "",
		"PASSWORD": "",
		"HOST": "localhost",
		"PORT": "",

	}
}

INSTALLED_APPS += ("debug_toolbar",)