# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=40)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['name', 'password']

    def __str__(self):
        return self.name


class ProfileFeedItem(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status_text
