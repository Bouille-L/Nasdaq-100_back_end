from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from api.models import ContactMessage

class SendEmailAPIViewTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.url = reverse('store_message')  # Replace 'store_message' with the actual URL name for SendEmailAPIView

    def test_send_email_api_view_post(self):
        """
        Test the POST method of SendEmailAPIView to ensure it creates a ContactMessage
        object and returns the correct response.
        """
        data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'message': 'This is a test message'
        }

        response = self.client.post(self.url, data, format='json')
        
        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Check if the response contains the expected message
        self.assertEqual(response.data, {"message": "Your message has been received. Thank you!"})

        # Check if a ContactMessage object has been created
        self.assertEqual(ContactMessage.objects.count(), 1)
        contact_message = ContactMessage.objects.first()
        self.assertEqual(contact_message.name, 'John Doe')
        self.assertEqual(contact_message.email, 'john@example.com')
        self.assertEqual(contact_message.message, 'This is a test message')
