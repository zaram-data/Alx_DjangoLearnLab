from .models import Book, Library, Author, Librarian

def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = Book.objects.filter(library=library)
    return books

def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)

def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return Librarian.objects.get(library=library)
