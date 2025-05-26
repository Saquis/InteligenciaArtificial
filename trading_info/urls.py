# trading_info/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path ('aprender', views.aprender_trading, name='aprender'),
]