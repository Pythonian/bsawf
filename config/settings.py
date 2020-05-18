import os
from datetime import timedelta
from distutils.util import strtobool

from celery.schedules import crontab
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
CELERYBEAT_SCHEDULE = {
    'mark-soon-to-expire-credit-cards': {
        'task': 'snakeeyes.blueprints.billing.tasks.mark_old_credit_cards',
        'schedule': crontab(hour=0, minute=0)
    },
    'expire-old-coupons': {
        'task': 'snakeeyes.blueprints.billing.tasks.expire_old_coupons',
        'schedule': crontab(hour=0, minute=1)
    },
}

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

# Stripe API keys for Billing
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', None)
STRIPE_PUBLISHABLE_KEY = os.getenv('STRIPE_PUBLISHABLE_KEY', None)
# https://stripe.com/docs/api/versioning
STRIPE_API_VERSION = os.getenv('STRIPE_API_VERSION')
STRIPE_CURRENCY = 'usd'
# Documentation for each plan field below can be found on Stripe's API docs:
# https://stripe.com/docs/api/plans/create
# After supplying both API keys and plans, you must sync the plans by running:
# snakeeyes stripe sync-plans
STRIPE_PLANS = {
    '0': {
        'id': 'bronze',
        'amount': 100,
        'currency': STRIPE_CURRENCY,
        'interval': 'month',
        'interval_count': 1,
        'trial_period_days': 14,
        'product': {
            'name': 'Bronze Plan',
            'type': 'service',
            'statement_descriptor': 'SNAKEEYES BRONZE'
        },
        'metadata': {}
    },
    '1': {
        'id': 'gold',
        'amount': 500,
        'currency': STRIPE_CURRENCY,
        'interval': 'month',
        'interval_count': 1,
        'trial_period_days': 14,
        'product': {
            'name': 'Gold Plan',
            'type': 'service',
            'statement_descriptor': 'SNAKEEYES GOLD'
        },
        'metadata': {
            'recommended': True
        }
    },
    '2': {
        'id': 'platinum',
        'amount': 1000,
        'currency': STRIPE_CURRENCY,
        'interval': 'month',
        'interval_count': 1,
        'trial_period_days': 14,
        'product': {
            'name': 'Platinum Plan',
            'type': 'service',
            'statement_descriptor': 'SNAKEEYES PLATINUM'
        },
        'metadata': {}
    }
}
