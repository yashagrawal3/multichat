# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Room

from django.contrib import admin

# Register your models here.

admin.site.register(
    Room,
    list_display=["id", "title", "staff_only"],
    list_display_links=["id", "title"],
)
