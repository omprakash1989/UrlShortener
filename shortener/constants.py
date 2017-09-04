# Constants for shortener APP.
from django.conf import settings

URL_SHORTENER_API_URL = '{}{}'.format(settings.DEFAULT_API_SITE_DOMAIN, 'api/v1/shortner/get-short-url/?url={}')
