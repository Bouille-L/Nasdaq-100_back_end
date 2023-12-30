from django.test import TestCase
from api.models import ContactMessage
from django.utils import timezone

class ContactMessageModelTest(TestCase):
    def setUp(self):
        """
        Set up a test environment for the model by creating a ContactMessage instance.
        """
        self.contact_message = ContactMessage.objects.create(
            name='John Doe',
            email='johndoe@example.com',
            message='This is a test message',
            created_at=timezone.now()
        )

    def test_contact_message_creation(self):
        """
        Test the creation of a ContactMessage instance and its properties.
        """
        self.assertEqual(self.contact_message.name, 'John Doe')
        self.assertEqual(self.contact_message.email, 'johndoe@example.com')
        self.assertEqual(self.contact_message.message, 'This is a test message')

    def test_contact_message_str(self):
        """
        Test the __str__ method of the ContactMessage model.
        """
        expected_object_name = f"Message from {self.contact_message.name}"
        self.assertEqual(str(self.contact_message), expected_object_name)
