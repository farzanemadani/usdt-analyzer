from django.contrib import admin
from .models import USDTPrice

@admin.register(USDTPrice)
class USDTPriceAdmin(admin.ModelAdmin):
    list_display = ['exchange', 'price', 'volume_24h', 'deviation', 'bubble_status', 'created_at']
    ordering     = ['-created_at']