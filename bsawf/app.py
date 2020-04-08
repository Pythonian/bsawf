from flask import Flask


def create_app():
    """
    Create a Flask application using the app factory instance.

    :return: Flask app
    """
    app = Flask(__name__)
    app.config.from_object('config.settings')

    @app.route('/')
    def index():
        """
        Render a Hello World response.

        :return: Flask response
        """
        return 'Hello World!'

    return app
