#!/bin/sh

python manage.py migrate

# superuser خودکار
echo "from django.contrib.auth import get_user_model; U = get_user_model(); U.objects.filter(username='admin').exists() or U.objects.create_superuser('admin', 'admin@email.com', 'admin123')" | python manage.py shell

celery -A config worker --loglevel=info &
celery -A config beat --loglevel=info &

gunicorn config.wsgi --log-file -