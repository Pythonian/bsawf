import os
from datetime import timedelta
from distutils.util import strtobool
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))), '.env'))

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = bool(strtobool(os.getenv('DEBUG')))
LOG_LEVEL = 'DEBUG'  # CRITICAL / ERROR / WARNING / INFO / DEBUG

SERVER_NAME = os.getenv('SERVER_NAME')

# Flask-Mail.
MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER')
MAIL_SERVER = os.getenv('MAIL_SERVER')
MAIL_PORT = int(os.getenv('MAIL_PORT'))
MAIL_USE_TLS = bool(strtobool(os.getenv('MAIL_USE_TLS')))
MAIL_USE_SSL = bool(strtobool(os.getenv('MAIL_USE_SSL')))
MAIL_USERNAME = os.getenv('MAIL_USERNAME')
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')

# Celery.
CELERY_BROKER_URL = os.getenv('REDIS_URL')
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_REDIS_MAX_CONNECTIONS = 5

# Flask-DebugToolbar
DEBUG_TB_INTERCEPT_REDIRECTS = False

ANALYTICS_GOOGLE_UA = os.getenv('ANALYTICS_GOOGLE_UA')

# SQLAlchemy
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Seed Admin User
SEED_ADMIN_EMAIL = os.getenv('SEED_ADMIN_EMAIL')
SEED_ADMIN_PASSWORD = os.getenv('SEED_ADMIN_PASSWORD')

# Flask-Login
REMEMBER_COOKIE_DURATION = timedelta(days=90)
