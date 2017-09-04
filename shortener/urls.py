# Urls conf for shortener APP.
from django.conf.urls import url
from shortener.views import UrlHandler


urlpatterns = [
    url(r'^get-short-url/', UrlHandler.as_view(), name='shorten_url'),
]
