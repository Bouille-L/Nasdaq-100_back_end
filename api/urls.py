# api/urls.py
from django.urls import path
from .views import NewsView, StockView
from .SendEmailAPI_View import SendEmailAPIView

urlpatterns = [
    path('news/', NewsView.as_view(), name='news'),
    path('stock/', StockView.as_view(), name='stock'),
    path('store_message/', SendEmailAPIView.as_view(), name='store_message'),
]
