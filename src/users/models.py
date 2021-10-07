# coding=utf-8
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(
        blank=False,
        unique=True,
        verbose_name='электронная почта',
    )  # forces user to fill email field
