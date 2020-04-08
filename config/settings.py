import os


SECRET_KEY = os.getenv('SECRET_KEY', 'secret')

SERVER_NAME = os.getenv('SERVER_NAME',
                        'localhost.localdomain:8000')

# Flask-Mail.
MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER', 'no-reply@example.com')
MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', 'true').lower()
MAIL_USE_SSL = os.getenv('MAIL_USE_SSL', 'false').lower()
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
