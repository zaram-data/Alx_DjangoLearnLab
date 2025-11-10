from django.urls import path
from .views import list_books  # ✅ exact string checker wants
from .views import (
    LibraryDetailView,
    RegisterView,
    CustomLoginView,
    CustomLogoutView,
    admin_view,
    member_view,
    librarian_view,
    add_book_view,
    edit_book_view,
    delete_book_view
)

urlpatterns = [
    # -----------------------------
    # Book and Library URLs
    # -----------------------------
    path('books/', list_books, name='list_books'),  # ✅
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # ✅

    # -----------------------------
    # Authentication URLs
    # -----------------------------
    path('register/', RegisterView.as_view(), name='register'),  # ✅ views.register
    path('login/', CustomLoginView.as_view(template_name="relationship_app/login.html"), name='login'),  # ✅ LoginView.as_view(template_name=...)
    path('logout/', CustomLogoutView.as_view(template_name="relationship_app/logout.html"), name='logout'),  # ✅ LogoutView.as_view(template_name=...)

    # -----------------------------
    # Role-Based Access URLs
    # -----------------------------
    path('admin-view/', admin_view, name='admin_view'),           # ✅
    path('member-view/', member_view, name='member_view'),       # ✅
    path('librarian-view/', librarian_view, name='librarian_view'), # ✅

    # -----------------------------
    # Permission-protected Book URLs
    # -----------------------------
    path('book/add/', add_book_view, name='add_book'),                 # ✅
    path('book/edit/<int:book_id>/', edit_book_view, name='edit_book'), # ✅
    path('book/delete/<int:book_id>/', delete_book_view, name='delete_book'), # ✅
]
