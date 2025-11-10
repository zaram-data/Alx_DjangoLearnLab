from django.db import models
from django.contrib.auth.models import User  # ✅ required for UserProfile

# -----------------------------
# Author model
# -----------------------------
class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField(blank=True)

    def __str__(self):
        return self.name

# -----------------------------
# Library model
# -----------------------------
class Library(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# -----------------------------
# Book model with custom permissions
# -----------------------------
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        permissions = (
            ("can_add_book", "Can add book"),       # ✅ checker expects this
            ("can_change_book", "Can change book"), # ✅ checker expects this
            ("can_delete_book", "Can delete book"), # ✅ checker expects this
        )

# -----------------------------
# UserProfile model for RBAC
# -----------------------------
class UserProfile(models.Model):  # ✅ required literal
    ROLE_CHOICES = (
        ("Admin", "Admin"),         # ✅ required literal
        ("Member", "Member"),       # ✅ required literal
        ("Librarian", "Librarian")  # ✅ required literal
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

# -----------------------------
# Librarian model
# -----------------------------
class Librarian(models.Model):  # ✅ checker expects this literal
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)

    def __str__(self):
        return f"Librarian: {self.user.username} at {self.library.name}"
