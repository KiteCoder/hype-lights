# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from hypertron.models import Venue, Show, Second, Pixel, SecondPixel, ContactPerson

# Register your models here.
admin.site.register(Venue)
admin.site.register(Show)
admin.site.register(Second)
admin.site.register(Pixel)
admin.site.register(SecondPixel)
admin.site.register(ContactPerson)
