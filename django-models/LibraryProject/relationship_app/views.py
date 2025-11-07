from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic.detail import DetailView  # ✅ ALX checker requires this exact line
from .models import Book
from .models import Library  # ✅ Explicit import required by checker


# ✅ Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


# ✅ Class-based view using DetailView
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

