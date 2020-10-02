from django.test import TestCase


class DemoTestCase(TestCase):

    def load_main_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
