from django.urls import path
from . import views

app_name = "api"

urlpatterns = [
    # List all books
    path("books/", views.ListView.as_view(), name="book-list"),

    # Create a book (POST)
    path("books/create/", views.CreateView.as_view(), name="book-create"),

    # Retrieve a single book (GET)
    path("books/<int:pk>/", views.DetailView.as_view(), name="book-detail"),

    # Update a book (PUT/PATCH)
    path("books/<int:pk>/update/", views.UpdateView.as_view(), name="book-update"),

    # Delete a book (DELETE)
    path("books/<int:pk>/delete/", views.DeleteView.as_view(), name="book-delete"),
]
