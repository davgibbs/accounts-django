from django.db import models
from django.contrib.auth.models import AbstractUser


class WMHUser(AbstractUser):
    nickname = models.CharField(max_length=64, verbose_name='Nick name')
