from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from unittest.mock import patch
import requests

class NewsAndStockViewTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.news_url = reverse('news')  # Replace 'news' with the actual URL name for NewsView

    @patch('requests.get')
    def test_get_news_success(self, mock_get):
        """
        Test the GET method of NewsView with a successful response from the external news API.
        """
        mock_response_data = {
            "data": [{
                "uuid": "some-uuid",
                "title": "Test News",
                "description": "Test Description",  # Ensure this field is included if your API returns it
                "snippet": "Test Snippet",
                "url": "http://example.com",
                "image_url": "http://example.com/image.jpg",
                "language": "en",
                "published_at": "2023-01-01T12:00:00Z",  # Adjust the format as per your actual response
                "source": "Test Source"
            }]
        }

        mock_get.return_value.json.return_value = mock_response_data
        mock_get.return_value.status_code = 200

        response = self.client.get(self.news_url)

        # Check if the response data matches the mocked data
        self.assertEqual(response.json(), mock_response_data['data'])

    @patch('requests.get')
    def test_get_news_failure(self, mock_get):
        """
        Test the GET method of NewsView with a failure response from the external news API.
        """
        mock_get.side_effect = requests.RequestException("API Error")

        response = self.client.get(self.news_url)

        # Check if the response status code is 500 Internal Server Error
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        # Check if the error message is correct
        self.assertEqual(response.json(), {"error": "Failed to fetch news data"})

    # You can add similar tests for StockView as well, following the same pattern.
