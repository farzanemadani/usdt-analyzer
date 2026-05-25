from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import USDTPrice
from .serializers import USDTPriceSerializer
from .services import fetch_and_save_price

@api_view(['GET'])
def latest_prices(request):
    """
    Retrieve the 20 most recent USDT price records.

    Returns:
        Response: A list of serialized USDTPrice objects.
    """
    prices = USDTPrice.objects.order_by('-created_at')[:20]
    serializer = USDTPriceSerializer(prices, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def fetch_now(request):
    """
    Fetch the current USDT price from CoinGecko and save it to the database.

    Returns:
        Response: The serialized data of the newly created record.
    """
    record = fetch_and_save_price()
    serializer = USDTPriceSerializer(record)
    return Response(serializer.data)

@api_view(['GET'])
def market_status(request):
    """
    Provide an overview of the current market status.

    Returns:
        Response: A dictionary containing price, deviation, bubble_status, 
                  and timestamp if data exists, otherwise an error message.
    """
    latest = USDTPrice.objects.order_by('-created_at').first()
    
    if not latest:
        return Response({"error": "No data available."})
    
    return Response({
        "price": latest.price,
        "deviation": latest.deviation,
        "status": latest.bubble_status,
        "updated_at": latest.created_at
    })