from django.test import TestCase
import requests
from shortener.constants import URL_SHORTENER_API_URL


# Shorten API test case.
class ShortenUrlTest(TestCase):

    def test_shorten_url_api_success(self):
        resp = requests.get(URL_SHORTENER_API_URL.format('http://google.co.in/'))
        self.assertEqual(resp.status_code, 200)

    def test_shorten_url_api_failure(self):
        resp = requests.get(URL_SHORTENER_API_URL.format('http://google.co.in/name=w we ew'))
        self.assertEqual(resp.status_code, 400)
