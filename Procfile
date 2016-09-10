web: gunicorn config.wsgi:application
worker: celery worker --app=teachmodern.taskapp --loglevel=info
