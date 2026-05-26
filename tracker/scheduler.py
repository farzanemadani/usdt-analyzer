from apscheduler.schedulers.background import BackgroundScheduler
from .services import fetch_and_save_price

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(fetch_and_save_price, 'interval', minutes=1)
    scheduler.start()