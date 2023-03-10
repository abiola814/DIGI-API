from django.db import models
from django.contrib.auth.models import AbstractUser

from customusermanager import CustomUserManager
# Create your models here.

class User(AbstractUser):
    """ Customer User model"""

    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    is_customer = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)

    objects = CustomUserManager()
