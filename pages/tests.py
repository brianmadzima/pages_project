from django.http import response
from django.test import SimpleTestCase

class TestSimpleCase(SimpleTestCase):
    def test_home_page_view(self):
        response = self.client.get('/')
        self.assertEqual = (response.status_code, 200)

    def test_about_page_view(self):
        response = self.client.get('/about/')
        self.assertEqual = (response.status_code, 200)
