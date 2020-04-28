from celery import Celery
from flask import Flask
from werkzeug.debug import DebuggedApplication

from snakeeyes.blueprints.user.models import User
from snakeeyes.register import (blueprints, error_templates, extensions,
                                middleware, exception_handler, authentication)

CELERY_TASK_LIST = [
    'snakeeyes.blueprints.contact.tasks',
    'snakeeyes.blueprints.user.tasks',
]


def create_celery_app(app=None):
    """
    Create a new Celery object and tie together the Celery config to the app's
    config. Wrap all tasks in the context of the application.

    :param app: Flask app
    :return: Celery app
    """
    app = app or create_app()

    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'],
                    include=CELERY_TASK_LIST)
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery


def create_app(settings_override=None):
    """
    Create a Flask application using the app factory pattern.

    :param settings_override: Override settings
    :return: Flask app
    """
    app = Flask(__name__, static_folder='../static', static_url_path='')

    app.config.from_object('config.settings')

    if settings_override:
        app.config.update(settings_override)

    # Register
    blueprints(app)
    extensions(app)
    authentication(app, User)
    middleware(app)
    error_templates(app)
    exception_handler(app)

    app.logger.setLevel(app.config['LOG_LEVEL'])

    if app.debug:
        app.wsgi_app = DebuggedApplication(app.wsgi_app, evalex=True)

    return app
