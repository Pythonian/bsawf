import logging
from logging.handlers import SMTPHandler

import stripe
from flask import render_template
from werkzeug.middleware.proxy_fix import ProxyFix

from snakeeyes.blueprints.admin import admin
from snakeeyes.blueprints.billing import billing, stripe_webhook
from snakeeyes.blueprints.billing.template_processors import (current_year,
                                                              format_currency)
from snakeeyes.blueprints.contact import contact
from snakeeyes.blueprints.page import page
from snakeeyes.blueprints.user import user
from snakeeyes.extensions import (
    csrf, db, debug_toolbar, login_manager, mail)

FLASK_BLUEPRINTS = [admin, page, contact, user, billing, stripe_webhook]

CUSTOM_ERROR_PAGES = [404, 500]


def authentication(app, user_model):
    """
    Initialize the Flask-Login extension (mutates the app passed in).

    :param app: Flask application instance
    :param user_model: Model that contains the authentication information
    :type user_model: SQLAlchemy model
    :return: None
    """
    login_manager.login_view = 'user.login'
    login_manager.login_message_category = 'danger'

    @login_manager.user_loader
    def load_user(uid):
        return user_model.query.get(uid)


def blueprints(app):
    """
    Register 0 or more blueprints (mutates the app passed in).

    :param app: Flask application instance
    :return: None
    """
    for blueprint in FLASK_BLUEPRINTS:
        app.register_blueprint(blueprint)

    return None


def extensions(app):
    """
    Register 0 or more extensions (mutates the app passed in).

    :param app: Flask application instance
    :return: None
    """
    debug_toolbar.init_app(app)
    mail.init_app(app)
    csrf.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    return None


def middleware(app):
    """
    Register 0 or more middleware (mutates the app passed in).

    :param app: Flask application instance
    :return: None
    """
    # Swap request.remote_addr with the real IP address even if behind a proxy.
    app.wsgi_app = ProxyFix(app.wsgi_app)

    return None


def error_templates(app):
    """
    Register 0 or more custom error pages (mutates the app passed in).

    :param app: Flask application instance
    :return: None
    """

    def render_status(status):
        """
         Render a custom template for a specific status.
           Source: http://stackoverflow.com/a/30108946

         :param status: Status as a written name
         :type status: str
         :return: None
         """
        # Get the status code from the status, default to a 500 so that we
        # catch all types of errors and treat them as a 500.
        code = getattr(status, 'code', 500)
        return render_template('errors/{0}.html'.format(code)), code

    for error in CUSTOM_ERROR_PAGES:
        app.errorhandler(error)(render_status)

    return None


def exception_handler(app):
    """
    Register 0 or more exception handlers (mutates the app passed in).

    :param app: Flask application instance
    :return: None
    """
    mail_handler = SMTPHandler((app.config.get('MAIL_SERVER'),
                                app.config.get('MAIL_PORT')),
                               app.config.get('MAIL_USERNAME'),
                               [app.config.get('MAIL_USERNAME')],
                               '[Exception handler] A 5xx was thrown',
                               (app.config.get('MAIL_USERNAME'),
                                app.config.get('MAIL_PASSWORD')),
                               secure=())

    mail_handler.setLevel(logging.ERROR)
    mail_handler.setFormatter(logging.Formatter("""
    Time:               %(asctime)s
    Message type:       %(levelname)s


    Message:

    %(message)s
    """))
    app.logger.addHandler(mail_handler)

    return None


def api_keys(app):
    """
    Register 0 or more API keys.

    :param app: Flask application instance
    :return: None
    """
    stripe.api_key = app.config.get('STRIPE_SECRET_KEY')
    stripe.api_version = app.config.get('STRIPE_API_VERSION')

    return None


def template_processors(app):
    """
    Register 0 or more custom template processors (mutates the app passed in).

    :param app: Flask application instance
    :return: App jinja environment
    """
    app.jinja_env.filters['format_currency'] = format_currency
    app.jinja_env.globals.update(current_year=current_year)

    return app.jinja_env
