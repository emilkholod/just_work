from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

client = APIClient()


# Create your tests here.
class TestAPI(TestCase):
    fixtures = ['initial_data.yaml']

    def test_page_list(self):
        response = client.get('/api/pages/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()['results']), 3)

    def test_page_instance(self):
        response = client.get('/api/pages/2/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()['content']), 2)

    def test_content_counter(self):
        client.get('/api/pages/2/')
        response = client.get('/api/pages/2/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        contents = response.json()['content']
        self.assertEqual(contents[0]['counter'], 2)
        self.assertEqual(contents[1]['counter'], 2)
