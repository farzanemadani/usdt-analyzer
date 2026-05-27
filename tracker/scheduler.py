from apscheduler.schedulers.background import BackgroundScheduler
from .services import fetch_and_save_price

def cleanup_old_prices():
    from .models import USDTPrice
    from django.utils import timezone
    from datetime import timedelta

    
    cutoff = timezone.now() - timedelta(days=1)
    deleted, _ = USDTPrice.objects.filter(created_at__lt=cutoff).delete()
    print(f"Cleaned up {deleted} old records")

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(fetch_and_save_price, 'interval', seconds=30)

    scheduler.add_job(cleanup_old_prices, 'cron', hour=3, minute=0)
    scheduler.start()
