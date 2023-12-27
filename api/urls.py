from django.urls import path
from .views import NewsView 
from.views import StockView


urlpatterns = [
    path('news/', NewsView.as_view(), name='news'),
    path('stock/', StockView.as_view(), name='stock'),
]
