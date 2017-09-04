# serialize and deserialize data

from rest_framework import serializers
from shortener.models import ShortUrls


class UrlShortnerSerializer(serializers.Serializer):
    url = serializers.URLField(required=True)

    class meta:
        model = ShortUrls
        fields = ['url', 'short_url']
