# relationship_app/urls.py
from django.urls import path
from .views import (
    list_books,
    LibraryDetailView,
    RegisterView,
    CustomLoginView,
    CustomLogoutView
)

urlpatterns = [
    # Book and library URLs
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Authentication URLs
    path('register/', RegisterView.as_view(), name='register'),   # views.register
    path('login/', CustomLoginView.as_view(), name='login'),       # LoginView.as_view(template_name=...)
    path('logout/', CustomLogoutView.as_view(), name='logout'),    # LogoutView.as_view(template_name=...)
]
