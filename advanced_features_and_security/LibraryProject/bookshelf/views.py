# LibraryProject/bookshelf/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book  # Make sure you have a Book model in models.py

# View for listing books with proper permission handling
@permission_required('bookshelf.view_book', raise_exception=True)
def book_list(request):
    # Fetch all Book objects
    books = Book.objects.all()
    
    # Pass the books to the template
    return render(request, 'bookshelf/book_list.html', {'books': books})
