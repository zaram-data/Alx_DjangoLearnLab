# CRUD Operations

## Create

>>> from bookshelf.models import Book
>>> book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
>>> book
# Output: <Book: 1984 by George Orwell (1949)>

## Retrieve
>>> Book.objects.all()
# Output: <QuerySet [<Book: 1984 by George Orwell (1949)>]>

## Update
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
>>> Book.objects.all()
# Output: <QuerySet [<Book: Nineteen Eighty-Four by George Orwell (1949)>]>

## Delete
>>> book.delete()
# Output: (1, {'bookshelf.Book': 1})
>>> Book.objects.all()
# Output: <QuerySet []>