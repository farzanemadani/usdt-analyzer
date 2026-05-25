from django.db import models

class USDTPrice(models.Model):
    exchange = models.CharField(max_length=100)      # Name of the exchange (Binance, Kraken, ...)
    price = models.FloatField()                       # USDT price in USD (e.g., 1.0023)
    volume_24h = models.FloatField(null=True, blank=True)  # 24-hour trading volume
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def deviation(self):
        """Distance from $1 in percentage"""
        return round((self.price - 1.0) * 100, 4)

    @property
    def bubble_status(self):
        """Status of the bubble"""
        d = abs(self.deviation)
        if d < 0.1:
            return "normal"      # normal
        elif d < 0.5:
            return "warning"     # warning
        else:
            return "bubble"      # bubble

    def __str__(self):
        return f"{self.exchange} | ${self.price} | {self.deviation:+.4f}%"