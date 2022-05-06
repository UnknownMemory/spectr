from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    country = models.TextField(blank=True)
    display_name = models.CharField(max_length=50, null=False)

class Profile(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    bio = models.CharField(max_length=255, blank=True)
    url = models.JSONField(blank=True)
    picture = models.URLField()

class Follow(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower")
    following_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")
    followed_at = models.DateTimeField(auto_now_add=True, blank=True)