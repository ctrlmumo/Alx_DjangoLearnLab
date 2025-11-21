from django.urls import path
from .views import list_books, LibraryDetailView
from .views import list_books, library_detail, login_view, logout_view, register_view

urlpatterns = [
    path('books/', list_books, name='list-books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register_view, name="register"),
]
