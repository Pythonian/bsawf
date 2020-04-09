web: gunicorn wsgi:app
worker: celery worker -A snakeeyes.blueprints.contact.tasks -l info