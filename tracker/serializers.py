from rest_framework import serializers
from .models import USDTPrice

class USDTPriceSerializer(serializers.ModelSerializer):
    deviation = serializers.FloatField(read_only=True)
    bubble_status = serializers.CharField(read_only=True)

    class Meta:
        model = USDTPrice
        fields = ['id', 'exchange', 'price', 'volume_24h', 'created_at', 'deviation', 'bubble_status']
