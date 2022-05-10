from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    country = models.TextField()
    display_name = models.CharField(max_length=50, null=False)


class Profile(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    bio = models.CharField(max_length=255)
    url = models.JSONField()
    picture = models.URLField()


class Follow(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower")
    following_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")
    followed_at = models.DateTimeField(auto_now_add=True, blank=True)


class Like(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_like")
    track_id = models.ForeignKey("audio.Track", on_delete=models.CASCADE, related_name="track_like")
    liked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["user_id", "track_id"], name="unique_like")]


class Notification(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_notification")
    subject_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="subject_notification"
    )
    object_id = models.ForeignKey(
        "audio.Track", on_delete=models.CASCADE, related_name="object_notification"
    )
    status = models.TextField()
    type = models.TextField()
