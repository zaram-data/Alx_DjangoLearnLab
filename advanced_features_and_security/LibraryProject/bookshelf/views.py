# LibraryProject/bookshelf/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book  # Make sure you have a Book model in models.py
from .forms import ExampleForm

# View for listing books with proper permission handling
@permission_required('bookshelf.view_book', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

# View to render the ExampleForm
def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Handle form submission here (e.g., save data, process input)
            # For now, just re-render the form after submission
            return render(request, 'bookshelf/form_example.html', {'form': form, 'success': True})
    else:
        form = ExampleForm()
    
    return render(request, 'bookshelf/form_example.html', {'form': form})

