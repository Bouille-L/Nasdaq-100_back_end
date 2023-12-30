from django.test import TestCase
from django.urls import reverse, resolve
from api.views import NewsView, StockView  # Import your views

class ProjectUrlsTest(TestCase):
    def test_admin_url(self):
        url = reverse('admin:index')
        self.assertEqual(resolve(url).func.__name__, 'index')

    def test_api_news_url(self):
        url = reverse('news')
        self.assertEqual(resolve(url).func.view_class, NewsView)

    def test_api_stock_url(self):
        url = reverse('stock')
        self.assertEqual(resolve(url).func.view_class, StockView)
