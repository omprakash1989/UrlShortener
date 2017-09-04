# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.views import APIView
from shortener.serializers import UrlShortnerSerializer
from rest_framework.response import Response
from rest_framework import status
from shortener.models import ShortUrls
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
import requests


class UrlHandler(APIView):
    """
    Handler for the url shorten request.
    """

    def get(self, request):
        """
        Get Request to fetch short url.
        :param request: API request.
        :return: Dict Response containing short url in short_url key.
        """
        response = {'status': False, "short_url": '', 'message': ''}
        url_serializer = UrlShortnerSerializer(data=request.GET)
        response_status = status.HTTP_200_OK
        if url_serializer.is_valid():
            try:
                # Check if already generated, serve it from DB.
                url = ShortUrls.objects.get(url=url_serializer.data.get("url"), is_active=True)
                response['short_url'] = url.short_url
                response['status'] = True

            except ObjectDoesNotExist:
                # Generate short url from bitly API and save in DB for further requests.
                short_url, api_status = self.generate_short_link(url_serializer.data.get("url"))
                if api_status:
                    ShortUrls(url=url_serializer.data.get("url"), short_url=short_url).save()
                    response['status'] = True
                    response['short_url'] = short_url
                else:
                    response['message'] = 'Oops..some error occurred.'
                    response_status = status.HTTP_400_BAD_REQUEST
        else:
            return Response(url_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(response, status=response_status)

    def generate_short_link(self, url):
        # Generates the short link for a given long/original url.
        # Uses bitly API.
        # @refer: http://dev.bitly.com/links.html#v3_shorten

        short_url = ''
        status = False
        try:
            # Put API request to generate short url.
            response = requests.get(settings.BASE_API_URL.format(settings.API_ACCESS_TOKEN, url))
            response_json = response.json()
            if response_json['status_code'] == 200:
                short_url = response_json['data']['url']
                status = True

        except (ValueError, KeyError):
            # Handle if required.
            pass

        return short_url, status

