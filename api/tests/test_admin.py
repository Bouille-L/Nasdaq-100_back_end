from django.test import TestCase
from django.contrib.admin.sites import AdminSite
from api.models import ContactMessage
from api.admin import ContactMessageAdmin

class ContactMessageAdminTest(TestCase):
    """
    Test case for the ContactMessageAdmin class to ensure that the admin settings for
    the ContactMessage model are correctly configured.
    """

    def setUp(self):
        """
        Set up method to create an instance of the admin site before each test is run.
        This method is automatically called before each test method.
        """
        self.site = AdminSite()

    def test_admin_list_display(self):
        """
        Test to ensure that the 'list_display' attribute in ContactMessageAdmin correctly
        specifies the fields to be displayed in the Django admin list view.
        """
        # Create an instance of ContactMessageAdmin
        ma = ContactMessageAdmin(ContactMessage, self.site)
        # Check if 'list_display' contains the correct fields
        self.assertEqual(ma.list_display, ('name', 'email', 'created_at'))

    def test_admin_list_filter(self):
        """
        Test to ensure that the 'list_filter' attribute in ContactMessageAdmin correctly
        specifies the fields to be used as filters in the Django admin list view.
        """
        # Create an instance of ContactMessageAdmin
        ma = ContactMessageAdmin(ContactMessage, self.site)
        # Check if 'list_filter' contains the correct field
        self.assertEqual(list(ma.list_filter), ['created_at'])

    def test_admin_search_fields(self):
        """
        Test to ensure that the 'search_fields' attribute in ContactMessageAdmin correctly
        specifies the fields to be used for the search functionality in the Django admin.
        """
        # Create an instance of ContactMessageAdmin
        ma = ContactMessageAdmin(ContactMessage, self.site)
        # Check if 'search_fields' contains the correct fields
        self.assertEqual(list(ma.search_fields), ['name', 'email', 'message'])
