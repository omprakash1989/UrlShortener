# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class ShortUrls(models.Model):
    # ShortUrls model which holds already generated short urls.
    id = models.AutoField(primary_key=True)
    url = models.URLField(max_length=255, unique=True, db_index=True, default='')
    short_url = models.URLField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __meta__(self):
        return self.short_url
