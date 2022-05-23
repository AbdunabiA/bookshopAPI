from django.conf import settings
from django.db import models
# from django.contrib.auth.models import AbstractUser
User = settings.AUTH_USER_MODEL
class CustomUser(models.Model):
    username = models.CharField(max_length=15, unique=True)
    email = models.EmailField('email', unique=True, blank=False, null=False)
    password = models.CharField(max_length=30, default='hello')
    first_name = models.CharField('First Name', max_length=255, blank=True,
                                  null=False)
    last_name = models.CharField('Last Name', max_length=255, blank=True,
                                 null=False)
    USERNAME_FIELD = 'username'

    def __str__(self):
        return f"{self.username}, {self.email} "