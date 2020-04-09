import os
from distutils.util import strtobool

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = True
LOG_LEVEL = 'DEBUG'  # CRITICAL / ERROR / WARNING / INFO / DEBUG

SERVER_NAME = os.getenv('SERVER_NAME')

# Flask-Mail.
MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER')
MAIL_SERVER = os.getenv('MAIL_SERVER')
MAIL_PORT = int(os.environ.get('MAIL_PORT'))
MAIL_USE_TLS = bool(strtobool(os.getenv('MAIL_USE_TLS')))
MAIL_USE_SSL = bool(strtobool(os.getenv('MAIL_USE_SSL')))
MAIL_USERNAME = os.getenv('MAIL_USERNAME')
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')

# Celery.
CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', 'redis://localhost:6379/0')
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_REDIS_MAX_CONNECTIONS = 5

# Flask-DebugToolbar
DEBUG_TB_INTERCEPT_REDIRECTS = False

SENTRY_SDK = os.getenv('SENTRY_SDK')

ANALYTICS_GOOGLE_UA = None
