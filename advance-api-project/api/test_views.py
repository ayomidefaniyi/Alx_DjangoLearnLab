from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Author, Book


class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )

        # Create author
        self.author = Author.objects.create(name="Ayomide Author")

        # Create books
        self.book1 = Book.objects.create(
            title="Python Basics",
            publication_year=2020,
            author=self.author
        )

        self.book2 = Book.objects.create(
            title="Django Advanced",
            publication_year=2022,
            author=self.author
        )

        self.list_url = reverse('book-list')

    # ✅ Test List Books
    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    # ✅ Test Create Book (requires authentication)
    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='testpass')

        data = {
            "title": "New Book",
            "publication_year": 2023,
            "author": self.author.id
        }

        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    # ❌ Test Create Book without authentication
    def test_create_book_unauthenticated(self):
        data = {
            "title": "Fail Book",
            "publication_year": 2023,
            "author": self.author.id
        }

        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # ✅ Test Update Book
    def test_update_book(self):
        self.client.login(username='testuser', password='testpass')

        url = reverse('book-detail', args=[self.book1.id])
        data = {
            "title": "Updated Title",
            "publication_year": 2020,
            "author": self.author.id
        }

        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    # ✅ Test Delete Book
    def test_delete_book(self):
        self.client.login(username='testuser', password='testpass')

        url = reverse('book-detail', args=[self.book1.id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # ✅ Test Filtering
    def test_filter_books(self):
        response = self.client.get(self.list_url + '?publication_year=2020')
        self.assertEqual(len(response.data), 1)

    # ✅ Test Searching
    def test_search_books(self):
        response = self.client.get(self.list_url + '?search=Python')
        self.assertEqual(len(response.data), 1)

    # ✅ Test Ordering
    def test_order_books(self):
        response = self.client.get(self.list_url + '?ordering=publication_year')
        self.assertEqual(response.data[0]['publication_year'], 2020)
