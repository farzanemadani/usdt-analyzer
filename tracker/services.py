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
    
    record = USDTPrice.objects.create(
        exchange="CoinGecko",
        price=price
    )
    
    print(f"Saved: ${price} | Deviation: {record.deviation:+.4f}%")
    return record