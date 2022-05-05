from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # username = models.CharField(max_length=20, null=False, unique=True)
    # email = models.EmailField(null=False, unique=True)
    # firstname = models.TextField(null=False)
    # lastname = models.TextField(null=False)
    country = models.TextField(blank=True)
    display_name = models.CharField(max_length=50, null=False)
    # created_at = models.DateTimeField(auto_now_add=True, blank=True)