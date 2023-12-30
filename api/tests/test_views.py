# api/tests/test_views.py

from rest_framework import status
from rest_framework.test import APITestCase
from unittest.mock import patch
import requests

class NewsAndStockViewTests(APITestCase):
    @patch("requests.get")
    def test_news_view_success(self, mock_get):
        # Mock the requests.get method to return a successful response
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [
            {
                "uuid": "c4c64aac-0ac4-482f-b00a-a2327a013225",
                "title": "Amazon notifies Prime Video users ads will start January 29",
                "snippet": "Amazon sent an email to millions of Prime Video users...",
                "url": "https://www.foxbusiness.com/markets/amazon-notifies-prime-video-users-ads-will-start-january-29",
                "image_url": "https://a57.foxnews.com/static.foxbusiness.com/foxbusiness.com/content/uploads/2023/09/0/0/Amazon-Prime-Video.jpg?ve=1&tl=1",
                "language": "en",
                "published_at": "2023-12-28T13:46:07-05:00",
                "source": "foxbusiness.com",
            },
            # Add more news items as needed
        ]

        # Make the API request
        response = self.client.get("/api/news/")

        # Assert the response status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert the response content matches the expected data structure
    expected_data = [
    {
        "uuid": "c4c64aac-0ac4-482f-b00a-a2327a013225",
        "title": "Amazon notifies Prime Video users ads will start January 29",
        "snippet": "Amazon sent an email to millions of Prime Video users...",
        "url": "https://www.foxbusiness.com/markets/amazon-notifies-prime-video-users-ads-will-start-january-29",
        "image_url": "https://a57.foxnews.com/static.foxbusiness.com/foxbusiness.com/content/uploads/2023/09/0/0/Amazon-Prime-Video.jpg?ve=1&tl=1",
        "language": "en",
        "published_at": "2023-12-28T13:46:07-05:00",
        "source": "foxbusiness.com",
    },
    # Add more expected news items as needed
    ]
    self.assertEqual(response.data, expected_data)

    @patch("requests.get")
    def test_stock_view_success(self, mock_get):
        # Mock the requests.get method to return a successful response
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            # Add stock data here
        }

        # Make the API request
        response = self.client.get("/api/stock/")

        # Assert the response status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert the response content matches the expected data structure
        expected_data = {
            # Add expected stock data here
        }
        self.assertEqual(response.data, expected_data)

    @patch("requests.get")
    def test_news_view_request_exception(self, mock_get):
        # Mock the requests.get method to raise a RequestException
        mock_get.side_effect = requests.RequestException("Test error")

        # Make the API request
        response = self.client.get("/api/news/")

        # Assert the response status code
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)

    @patch("requests.get")
    def test_stock_view_request_exception(self, mock_get):
        # Mock the requests.get method to raise a RequestException
        mock_get.side_effect = requests.RequestException("Test error")

        # Make the API request
        response = self.client.get("/api/stock/")

        # Assert the response status code
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
