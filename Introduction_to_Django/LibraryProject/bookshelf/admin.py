from django.contrib import admin
from .models import Book

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # columns to display
    list_filter = ('publication_year', 'author')  # add filters in the sidebar
    search_fields = ('title', 'author')  # enable search by title or author
