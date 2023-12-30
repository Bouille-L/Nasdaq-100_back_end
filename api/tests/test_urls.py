from django.test import TestCase
from django.urls import reverse
from rest_framework import status

class UrlsTests(TestCase):
    def test_news_url(self):
        url = reverse('news')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_stock_url(self):
        url = reverse('stock')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
