from django.urls import path
from . import views
urlpatterns = [
    path('prices/', views.latest_prices),
    path('fetch/', views.fetch_now),
    path('status/', views.market_status),
]