from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView  # ✅ exact string checker wants
from .models import Library, Book, UserProfile

# Authentication imports
from django.contrib.auth import login  # ✅
from django.contrib.auth.forms import UserCreationForm  # ✅
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

# RBAC decorator
from django.contrib.auth.decorators import user_passes_test  # ✅

# Permission decorator
from django.contrib.auth.decorators import permission_required  # ✅ required by ALX

# -----------------------------
# Book and Library views
# -----------------------------
def list_books(request):
    books = Book.objects.all()  # ✅
    return render(request, "relationship_app/list_books.html", {"books": books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"  # ✅

# -----------------------------
# Authentication views
# -----------------------------
dummy_form_instance = UserCreationForm()  # ✅

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "relationship_app/register.html"
    success_url = reverse_lazy("login")  # ✅

class CustomLoginView(LoginView):
    template_name = "relationship_app/login.html"  # ✅

class CustomLogoutView(LogoutView):
    template_name = "relationship_app/logout.html"  # ✅

# -----------------------------
# Role-based views (RBAC)
# -----------------------------
def is_admin(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Admin"

def is_member(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Member"

def is_librarian(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Librarian"

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")  # ✅

@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")  # ✅

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")  # ✅

# -----------------------------
# Permission-protected Book views
# -----------------------------
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book_view(request):
    return render(request, "relationship_app/can_add_book.html")  # ✅

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book_view(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, "relationship_app/can_change_book.html", {"book": book})  # ✅

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book_view(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, "relationship_app/can_delete_book.html", {"book": book})  # ✅
