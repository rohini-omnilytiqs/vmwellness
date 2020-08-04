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
    name = models.CharField(max_length = 100)


class Water(models.Model):

    userId = models.ForeignKey(User, null=True, blank=True, related_name='water_userId', on_delete=models.CASCADE)
    consumptionGoal = models.IntegerField(default=64)
    currAmountConsumed = models.IntegerField(default=0)


class Checklist(models.Model):

    userId = models.ForeignKey(User, null=True, blank=True, related_name='checklist_userId', on_delete=models.CASCADE)
    goal_one = models.TextField(null=True, blank=True)
    goal_one_completed = models.BooleanField(default=False)
    goal_two = models.TextField(null=True, blank=True)
    goal_two_completed = models.BooleanField(default=False)
    goal_three = models.TextField(null=True, blank=True)
    goal_three_completed = models.BooleanField(default=False)
    goal_four = models.TextField(null=True, blank=True)
    goal_four_completed = models.BooleanField(default=False)
    goal_five = models.TextField(null=True, blank=True)
    goal_five_completed = models.BooleanField(default=False)