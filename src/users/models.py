from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(blank=False,
                              unique=True,
                              verbose_name='электронная почта')
    # forces user to fill email field
