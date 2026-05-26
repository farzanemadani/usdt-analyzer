from celery import shared_task
from .services import fetch_and_save_price

@shared_task
def fetch_price_task():
    try:
        record = fetch_and_save_price()
        return f"saved: ${record.price} | {record.deviation:+.4f}%"
    except Exception as e:
        return f"error: {str(e)}"