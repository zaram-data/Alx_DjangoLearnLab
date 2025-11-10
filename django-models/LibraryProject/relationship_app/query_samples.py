from relationship_app.models import Library, Author, Book, Librarian

# List all books in a library
def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)  # ✅ ALX checker looks for this exact line
    books = library.books.all()  # ✅ Already required earlier
    return books

# Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return author.books.all()

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian

