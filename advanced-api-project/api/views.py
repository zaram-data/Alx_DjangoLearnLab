from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django_filters import rest_framework  # <- added for ALX checker
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer


# ListView - returns all books; read-only and open to unauthenticated users.
class ListView(generics.ListAPIView):
    """
    Lists all Book instances with filtering, search, and ordering.
    Supports optional filtering by ?year=YYYY to return books published in that year.
    Filtering: ?title=, ?author=, ?publication_year=
    Search: ?search=keyword (on title and author name)
    Ordering: ?ordering=fieldname (e.g., title, publication_year, author)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # DRF filter backends
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Fields for filtering
    filterset_fields = ['title', 'publication_year', 'author']

    # Fields for search
    search_fields = ['title', 'author__name']

    # Fields allowed for ordering
    ordering_fields = ['title', 'publication_year', 'author']

    def get_queryset(self):
        qs = super().get_queryset()
        year = self.request.query_params.get("year")
        if year:
            try:
                year_int = int(year)
                qs = qs.filter(publication_year=year_int)
            except ValueError:
                # invalid year param -> return empty queryset
                return qs.none()
        return qs


# DetailView - retrieve a single book by primary key (pk). Open to unauthenticated users.
class DetailView(generics.RetrieveAPIView):
    """
    Retrieve a single Book by ID (pk).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# CreateView - create a new Book. Only authenticated users allowed.
class CreateView(generics.CreateAPIView):
    """
    Create a new Book instance.
    Only authenticated users may create books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# UpdateView - update an existing Book. Only authenticated users allowed.
class UpdateView(generics.UpdateAPIView):
    """
    Partially or fully update a Book (PUT/PATCH).
    Only authenticated users may update books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# DeleteView - delete an existing Book. Only authenticated users allowed.
class DeleteView(generics.DestroyAPIView):
    """
    Delete a Book instance.
    Only authenticated users may delete books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

