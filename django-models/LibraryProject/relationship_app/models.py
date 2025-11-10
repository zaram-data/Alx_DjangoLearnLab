from django.db import models
from django.contrib.auth.models import User  # ✅ required for UserProfile

# -----------------------------
# Existing models
# -----------------------------
class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Library(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# -----------------------------
# UserProfile model for role-based access
# -----------------------------
class UserProfile(models.Model):  # ✅ required literal
    ROLE_CHOICES = (
        ("Admin", "Admin"),     # ✅ required literal
        ("Member", "Member"),   # ✅ required literal
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # one-to-one link
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
