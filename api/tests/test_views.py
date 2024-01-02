import json
import requests
from unittest.mock import patch
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse


# Test suite for the NewsView
class NewsViewTests(APITestCase):

    @patch('requests.get')
    def test_get_news_success(self, mock_get):
         # Mocking the successful API response for the news endpoint
        mock_response = mock_get.return_value
        mock_response.raise_for_status.side_effect = None
        # Defining a mock response that mimics the structure of the expected API response
        mock_response.json.return_value = {
            "data": [
                {
                    "uuid": "example-uuid-1",
                    "title": "Test News 1",
                    "snippet": "Test Snippet 1",
                    "url": "http://example.com/news1",
                    "image_url": "http://example.com/image1.jpg",
                    "language": "en",
                    "published_at": "2024-01-01T00:00:00Z",
                    "source": "example.com"
                },
                {
                    "uuid": "example-uuid-2",
                    "title": "Test News 2",
                    "snippet": "Test Snippet 2",
                    "url": "http://example.com/news2",
                    "image_url": "http://example.com/image2.jpg",
                    "language": "en",
                    "published_at": "2024-01-02T00:00:00Z",
                    "source": "example.com"
                }
            ]
        }

        # Get the URL for the stock endpoint
        url = reverse('news')
        # Perform a GET request to the stock endpoint
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
         # Checking each key in the response to ensure it matches the expected structure
        for news_item in response.json():
            self.assertIn("uuid", news_item)
            self.assertIn("title", news_item)
            self.assertIn("snippet", news_item)
            self.assertIn("url", news_item)
            self.assertIn("image_url", news_item)
            self.assertIn("language", news_item)
            self.assertIn("published_at", news_item)
            self.assertIn("source", news_item)

    @patch('requests.get')
    def test_get_news_failure(self, mock_get):
        # Mock API failure
        mock_get.side_effect = requests.RequestException

        url = reverse('news')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertIn("error", response.json())

# Test suite for the StockView
class StockViewTests(APITestCase):

    @patch('requests.get')
    def test_get_stock_success(self, mock_get):
        # Mocking the successful API response for Stock
        mock_response = mock_get.return_value
        mock_response.raise_for_status.side_effect = None
        # Adjust this to match the actual stock API response format
        mock_response.json.return_value = {
            "Meta Data": {
                # ... metadata fields
            },
            "Time Series (30min)": {
                "2023-12-29 15:30:00": {
                    "1. open": "50.8600",
                    "2. high": "50.8600",
                    "3. low": "50.4300",
                    "4. close": "50.7100",
                    "5. volume": "7111769"
                },
            }
        }

        # Using Django's reverse function to get the URL for the stock endpoint
        url = reverse('stock')
        # Making a GET request to the stock endpoint
        response = self.client.get(url)

        # Assertions to ensure the response is as expected
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Meta Data", response.json())
        self.assertIn("Time Series (30min)", response.json())

        # Additional assertions can be added to check specific stock data points

    @patch('requests.get')
    def test_get_stock_failure(self, mock_get):
        # Mocking API failure for Stock
        mock_get.side_effect = requests.RequestException

        # Using Django's reverse function to get the URL for the stock endpoint
        url = reverse('stock')
        # Making a GET request to the stock endpoint
        response = self.client.get(url)

        # Assertions to check the handling of errors
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertIn("error", response.json())