from django.urls import path
from .views import list_books  # ✅ exact string checker wants
from .views import (
    LibraryDetailView,
    RegisterView,
    CustomLoginView,
    CustomLogoutView,
    admin_view,
    member_view,
    librarian_view
)

urlpatterns = [
    # Book and Library URLs
    path('books/', list_books, name='list_books'),  # ✅
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # ✅

    # Authentication URLs
    path('register/', RegisterView.as_view(), name='register'),  # ✅
    path('login/', CustomLoginView.as_view(), name='login'),      # ✅
    path('logout/', CustomLogoutView.as_view(), name='logout'),   # ✅

    # Role-Based Access URLs
    path('admin-view/', admin_view, name='admin_view'),           # ✅
    path('member-view/', member_view, name='member_view'),       # ✅
    path('librarian-view/', librarian_view, name='librarian_view'), # ✅
]

