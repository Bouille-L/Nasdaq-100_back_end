# api/tests/test_serializers.py
from django.test import TestCase
from api.serializers import NewsSerializer

class NewsSerializerTest(TestCase):
    def test_serializer_valid_data(self):
        """
        Test case for validating the NewsSerializer with valid data.
        This test ensures that the serializer correctly validates data that
        meet all required fields and constraints.
        """
        # Define a dictionary with valid data that should pass the serializer validation
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

        # Create an instance of the serializer with the valid data
        serializer = NewsSerializer(data=valid_data)
        # Assert that the serializer deems the data as valid
        self.assertTrue(serializer.is_valid())

    def test_serializer_invalid_data(self):
        """
        Test case for validating the NewsSerializer with invalid data.
        This test checks that the serializer correctly identifies data as invalid
        if it does not meet the required fields or constraints.
        """
        # Define a dictionary with incomplete data that should fail the serializer validation
        invalid_data = {
            # Missing some required fields such as 'title' and 'description'
            "uuid": "some_uuid",
            "snippet": "Test Snippet",
            "url": "http://example.com",
            "image_url": "http://example.com/image.jpg",
            "language": "en",
            "published_at": "2023-01-01T12:00:00Z",
            "source": "Test Source"
        }

        # Create an instance of the serializer with the invalid data
        serializer = NewsSerializer(data=invalid_data)
        # Assert that the serializer deems the data as invalid
        self.assertFalse(serializer.is_valid())
