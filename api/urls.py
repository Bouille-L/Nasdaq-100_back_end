# api/urls.py
from django.urls import path
from .views import NewsView, StockViewTQQQ, StockViewSQQQ, StockViewQQQ
from .SendEmailAPI_View import SendEmailAPIView

urlpatterns = [
    path('news/', NewsView.as_view(), name='news'),
    path('TQQQ/', StockViewTQQQ.as_view(), name='TQQQ'),
    path('SQQQ/', StockViewSQQQ.as_view(), name='SQQQ'),
    path('QQQ/', StockViewQQQ.as_view(), name='QQQ'),
    path('store_message/', SendEmailAPIView.as_view(), name='store_message'),
]
