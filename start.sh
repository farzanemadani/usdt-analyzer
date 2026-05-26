#!/bin/sh

python manage.py migrate


python manage.py shell << 'EOF'
from django_celery_beat.models import PeriodicTask, CrontabSchedule
import json

schedule, _ = CrontabSchedule.objects.get_or_create(
    minute='*',
    hour='*',
    day_of_week='*',
    day_of_month='*',
    month_of_year='*',
)

PeriodicTask.objects.get_or_create(
    name='fetch-usdt-price',
    defaults={
        'crontab': schedule,
        'task': 'tracker.tasks.fetch_price_task',
        'args': json.dumps([]),
    }
)
print("Schedule registered!")
EOF


celery -A config worker --loglevel=info &
celery -A config beat --loglevel=info &

gunicorn config.wsgi --log-file -