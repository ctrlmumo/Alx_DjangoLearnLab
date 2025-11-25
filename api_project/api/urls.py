from django.urls import path
from .views import BookList
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'), # List all books
]