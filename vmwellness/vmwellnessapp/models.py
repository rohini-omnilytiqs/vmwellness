import os
import time
from datetime import timedelta

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, UserManager


class Activies(models.Model):

    userId = models.ForeignKey(User, null=True, blank=True, related_name='activities_userId', on_delete=models.CASCADE)
    post_time = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length = 140)
    anon = models.BooleanField(default = True)
    name = models.CharField(max_length = 100, null=True, blank=True)


class Water(models.Model):

    userId = models.ForeignKey(User, null=True, blank=True, related_name='water_userId', on_delete=models.CASCADE)
    consumptionGoal = models.IntegerField(default=64)
    currAmountConsumed = models.IntegerField(default=0)

class Checklist(models.Model):

    userId = models.ForeignKey(User, null=True, blank=True, related_name='checklist_userId', on_delete=models.CASCADE)
    goal = models.TextField()