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

echo "from django.contrib.auth import get_user_model; U = get_user_model(); U.objects.filter(username='admin').exists() or U.objects.create_superuser('admin', 'admin@email.com', 'admin123')" | python manage.py shell

celery -A config worker --loglevel=info &
celery -A config beat --loglevel=info &

gunicorn config.wsgi --log-file -