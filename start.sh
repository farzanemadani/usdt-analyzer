#!/bin/sh

# migration
python manage.py migrate

# celery worker در background
celery -A config worker --loglevel=info &

# celery beat در background
celery -A config beat --loglevel=info &

# gunicorn اصلی
gunicorn config.wsgi --log-file -