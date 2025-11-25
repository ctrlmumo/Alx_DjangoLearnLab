from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from api.models import Book

# tests for API endpoints
class BookAPITestCase(APITestCase):

    def setUp(self):
        # create user for authentication tests
        self.user = User.objects.create_user(username="tester", password="pass1234")
        self.client = APIClient()

        # API endpoints
        self.list_url = reverse('book-list')   # GET, POST
        # Detail URL created dynamically inside tests

        # sample 
        self.book1 = Book.objects.create(
            title="Django for APIs",
            author="William",
            publication_year=2020
        )
        self.book2 = Book.objects.create(
            title="Python Tricks",
            author="Dan Bader",
            publication_year=2018
        )

    # Authentication Tests
    def test_auth_required_for_list(self):
        #Ensure authentication is required.
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_login_authentication(self):
        #Test login with valid credentials.
        login = self.client.login(username="tester", password="pass1234")
        self.assertTrue(login)

    def test_authenticated_user_can_access_list(self):
        #Logged-in users should access book list.
        self.client.force_authenticate(user=self.user)

        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    # CRUD Tests
    def test_create_book(self):
        #Create a book and verify data.
        self.client.force_authenticate(user=self.user)
        payload = {
            "title": "New Book",
            "author": "Gloria",
            "publication_year": 2024
        }

        response = self.client.post(self.list_url, payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.get(title="New Book").author, "Gloria")

    def test_update_book(self):
        self.client.force_authenticate(user=self.user)
        detail_url = reverse('book-detail', args=[self.book1.id])

        payload = {
            "title": "Updated Title",
            "author": "William",
            "publication_year": 2020
        }
        response = self.client.put(detail_url, payload)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    def test_delete_book(self):
        self.client.force_authenticate(user=self.user)
        detail_url = reverse('book-detail', args=[this.book1.id])

        response = self.client.delete(detail_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # Filtering, Searching, Ordering
    def test_filter_books_by_year(self):
        """Test DRF filtering backend for publication_year."""
        self.client.force_authenticate(user=self.user)

        response = self.client.get(self.list_url, {"publication_year": 2020})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Django for APIs")

    def test_search_books(self):
        """Search by title or author."""
        self.client.force_authenticate(user=self.user)

        response = self.client.get(self.list_url, {"search": "Python"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Python Tricks")

    def test_order_books(self):
        """Order by publication_year."""
        self.client.force_authenticate(user=self.user)

        response = self.client.get(self.list_url, {"ordering": "-publication_year"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # book1 (2020) should come before book2 (2018)
        self.assertEqual(response.data[0]["title"], "Django for APIs")
