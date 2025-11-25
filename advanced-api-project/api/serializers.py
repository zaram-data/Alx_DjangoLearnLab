from rest_framework import serializers
from .models import Author, Book
import datetime


# Serializer for Book model with validation to prevent future publication years.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "publication_year", "author"]

    # Custom validation to ensure publication year is not in the future
    def validate_publication_year(self, value):
        current_year = datetime.datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# Author serializer includes nested books using BookSerializer.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Nested relationship

    class Meta:
        model = Author
        fields = ["id", "name", "books"]
