#!/bin/sh

python manage.py migrate


celery -A config worker --loglevel=info --beat &

gunicorn config.wsgi --log-file -