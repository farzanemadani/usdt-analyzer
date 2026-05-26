#!/bin/sh

# migration
python manage.py migrate


celery -A config worker --loglevel=info &


celery -A config beat --loglevel=info &


gunicorn config.wsgi --log-file -