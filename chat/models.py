# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from channels import Group

from django.db import models
from django.utils.six import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Room(models.Model):
    """
    A room for people to chat in.
    """

    # Room title
    title = models.CharField(max_length=255)

    # If only "staff" users are allowed (is_staff on django's User)
    staff_only = models.BooleanField(default=False)
    @property
    def websocket_group(self):
        """
        Returns the Channels Group that sockets should subscribe to to get sent
        messages as they are generated.
        """
        return Group("room-%s" % self.id)

    def __str__(self):
        return self.title
