import requests
from .models import USDTPrice

COINGECKO_URL = "https://api.coingecko.com/api/v3/simple/price"

def fetch_and_save_price():
    """
    Fetch price and save to database
    """
    params = {
        "ids": "tether",
        "vs_currencies": "usd",
        "include_24hr_vol": "true"
    }
    
    response = requests.get(COINGECKO_URL, params=params, timeout=10)
    data = response.json()

    price = data["tether"]["usd"]
    volume_24h = data["tether"]["usd_24h_vol"]
    
    record = USDTPrice.objects.create(
        exchange="CoinGecko",
        price=price,
        volume_24h=volume_24h,
    )
    
    print(f"Saved: ${price} | Volume 24h: {volume_24h} | Deviation: {record.deviation:+.4f}%")
    return record
