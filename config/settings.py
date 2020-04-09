import os

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = True
LOG_LEVEL = 'DEBUG'  # CRITICAL / ERROR / WARNING / INFO / DEBUG

# SERVER_NAME = os.getenv('SERVER_NAME',
#                         'localhost.localdomain:8000')

# Flask-Mail.
MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER', 'no-reply@example.com')
MAIL_SERVER = 'smtp.mailtrap.io'
MAIL_PORT = 2525
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = '93dad87dab41b7'
MAIL_PASSWORD = '3d2294bed0d58f'

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
