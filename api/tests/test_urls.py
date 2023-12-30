from django.test import TestCase
from django.urls import reverse
from rest_framework import status

class UrlsTests(TestCase):

    def test_news_url(self):
        # Reverse the 'news' URL and perform a GET request to it
        url = reverse('news')
        response = self.client.get(url)
        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_stock_url(self):
        # Reverse the 'stock' URL and perform a GET request to it
        url = reverse('stock')
        response = self.client.get(url)
        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_store_message_url_get(self):
        # Reverse the 'store_message' URL and perform a GET request to it
        url = reverse('store_message')
        response = self.client.get(url)
        # Expect a 405 Method Not Allowed, as the view does not support GET
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_store_message_url_post(self):
        # Reverse the 'store_message' URL and perform a POST request to it
        url = reverse('store_message')
        # Define the data to send in the POST request
        data = {
            'name': 'Test Name',
            'email': 'test@example.com',
            'message': 'Test message'
        }
        response = self.client.post(url, data, format='json')
        # Check if the response status code is 200 OK
        # This assumes the API endpoint is configured to return 200 OK after a successful POST
        self.assertEqual(response.status_code, status.HTTP_200_OK)
