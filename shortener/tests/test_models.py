from django.test import TestCase
from shortener.models import ShortUrls


# models test
class ShortUrlsTest(TestCase):

    def save_short_url(self, long_url="http://google.co.in/", short_url="http://bit.ly/2eUm2lV"):
        return ShortUrls.objects.create(url=long_url, short_url=short_url)

    def test_short_url_creation(self):
        saved_instance = self.save_short_url()
        self.assertTrue(isinstance(saved_instance, ShortUrls))
        self.assertEqual(saved_instance.__meta__(), saved_instance.short_url)
