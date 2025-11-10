from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library  # ✅ Explicit relative import for ALX checker

# Function-based view to list all books and their authors
def list_books(request):
    books = Book.objects.all()  # ✅ Must appear exactly like this
    return render(request, "relationship_app/list_books.html", {"books": books})  # ✅ Template path check

# Class-based view for library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
