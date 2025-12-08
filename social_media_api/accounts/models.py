# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    # If you plan to upload images, Pillow must be installed.
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    # followers: users that follow this user
    followers = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='following',
        blank=True
    )

    def __str__(self):
        return self.username
