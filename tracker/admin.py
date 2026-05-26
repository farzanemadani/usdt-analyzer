from django.contrib import admin
from .models import USDTPrice

@admin.register(USDTPrice)
class USDTPriceAdmin(admin.ModelAdmin):
    list_display  = ['exchange', 'price', 'deviation', 'bubble_status', 'created_at']
    list_filter   = ['bubble_status', 'exchange']
    ordering      = ['-created_at']