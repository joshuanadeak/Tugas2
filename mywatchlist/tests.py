from django.test import TestCase, Client
from django.urls import reverse, resolve

class MyWatchListTest(TestCase):
    def html_test_route(self):
        resp = Client().get('/mywatchlist/html/')
        self.assertEqual(resp.status_code, 200)

    def xml_test_route(self):
        resp = Client().get('/mywatchlist/xml/')
        self.assertEqual(resp.status_code, 200)

    def json_test_route(self):
        resp = Client().get('/mywatchlist/json/')
        self.assertEqual(resp.status_code, 200)