from django.db import models

# Author model stores information about book authors.
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Book model represents books written by authors.
# It has a ForeignKey to Author to create a One-to-Many relationship.
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
