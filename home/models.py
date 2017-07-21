# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.


class UserProfile(AbstractBaseUser):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
