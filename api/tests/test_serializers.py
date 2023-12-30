# api/tests/test_serializers.py
from django.test import TestCase
from api.serializers import NewsSerializer

class NewsSerializerTest(TestCase):
    def test_serializer_valid_data(self):
        # Test case for validating serializer with valid data
        valid_data = {
            "uuid": "some_uuid",
            "title": "Test Title",
            "description": "Test Description",
            "snippet": "Test Snippet",
            "url": "http://example.com",
            "image_url": "http://example.com/image.jpg",
            "language": "en",
            "published_at": "2023-01-01T12:00:00Z",
            "source": "Test Source"
        }

        serializer = NewsSerializer(data=valid_data)
        self.assertTrue(serializer.is_valid())

    def test_serializer_invalid_data(self):
        # Test case for validating serializer with invalid data
        invalid_data = {
            # Some required fields are missing
            "uuid": "some_uuid",
            "snippet": "Test Snippet",
            "url": "http://example.com",
            "image_url": "http://example.com/image.jpg",
            "language": "en",
            "published_at": "2023-01-01T12:00:00Z",
            "source": "Test Source"
        }

        serializer = NewsSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
