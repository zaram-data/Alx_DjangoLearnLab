from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Author, Book
from .serializers import BookSerializer

class BookAPITestCase(APITestCase):
    """
    Test suite for Book API endpoints: CRUD, filtering, search, ordering, permissions.
    """

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpass123")
        self.client = APIClient()

        # Create authors
        self.author1 = Author.objects.create(name="Author One")
        self.author2 = Author.objects.create(name="Author Two")

        # Create books
        self.book1 = Book.objects.create(title="Book One", publication_year=2020, author=self.author1)
        self.book2 = Book.objects.create(title="Book Two", publication_year=2021, author=self.author2)

        # API endpoints
        self.list_url = reverse("api:book-list")
        self.create_url = reverse("api:book-create")
        self.detail_url = lambda pk: reverse("api:book-detail", args=[pk])
        self.update_url = lambda pk: reverse("api:book-update", args=[pk])
        self.delete_url = lambda pk: reverse("api:book-delete", args=[pk])

    # --------------------
    # Read / List / Detail
    # --------------------
    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_book_detail(self):
        response = self.client.get(self.detail_url(self.book1.pk))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book1.title)

    # --------------------
    # Create
    # --------------------
    def test_create_book_unauthenticated(self):
        data = {"title": "New Book", "publication_year": 2023, "author": self.author1.pk}
        response = self.client.post(self.create_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_book_authenticated(self):
        self.client.login(username="testuser", password="testpass123")
        data = {"title": "New Book", "publication_year": 2023, "author": self.author1.pk}
        response = self.client.post(self.create_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "New Book")

    # --------------------
    # Update
    # --------------------
    def test_update_book_authenticated(self):
        self.client.login(username="testuser", password="testpass123")
        data = {"title": "Updated Book"}
        response = self.client.patch(self.update_url(self.book1.pk), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Book")

    def test_update_book_unauthenticated(self):
        data = {"title": "Updated Book"}
        response = self.client.patch(self.update_url(self.book1.pk), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # --------------------
    # Delete
    # --------------------
    def test_delete_book_authenticated(self):
        self.client.login(username="testuser", password="testpass123")
        response = self.client.delete(self.delete_url(self.book1.pk))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(pk=self.book1.pk).exists())

    def test_delete_book_unauthenticated(self):
        response = self.client.delete(self.delete_url(self.book1.pk))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # --------------------
    # Filtering, Searching, Ordering
    # --------------------
    def test_filter_books_by_publication_year(self):
        response = self.client.get(f"{self.list_url}?publication_year=2020")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], self.book1.title)

    def test_search_books_by_title(self):
        response = self.client.get(f"{self.list_url}?search=Book Two")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], self.book2.title)

    def test_order_books_by_title(self):
        response = self.client.get(f"{self.list_url}?ordering=title")
        titles = [b["title"] for b in response.data]
        self.assertEqual(titles, sorted(titles))
