web: gunicorn wsgi:app
worker: celery worker -B -A snakeeyes.blueprints.contact.tasks -l info