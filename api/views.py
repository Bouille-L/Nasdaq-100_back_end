from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import NewsSerializer
import requests
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

class NewsView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            url = settings.NEWS_API_URL
            response = requests.get(url)
            response.raise_for_status()  # Raise HTTPError for bad responses
            news_data = response.json().get("data", [])
        except requests.RequestException as e:
            logger.error(f"Error fetching news data: {e}")
            news_data = []

        serializer = NewsSerializer(data=news_data, many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class StockView(APIView):
    def get(self, request):
        try:
            url = settings.STOCK_API_URL
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
        except requests.RequestException as e:
            logger.error(f"Error fetching stock data: {e}")
            data = {}

        return Response(data)
