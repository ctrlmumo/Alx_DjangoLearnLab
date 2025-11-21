from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', views.list_books, name='list-books'),
    path('library/<int:pk>/', views.library_detail, name='library-detail'),

    # Auth required by checker
    path('login/', 
         LoginView.as_view(template_name='relationship_app/login.html'), 
         name='login'),

    path('logout/', 
         LogoutView.as_view(template_name='relationship_app/logout.html'), 
         name='logout'),

    path('register/', views.register, name='register'),

    path('admin-role/', views.admin_view, name='admin-view'),
    path('librarian-role/', views.librarian_view, name='librarian-view'),
    path('member-role/', views.member_view, name='member-view'),

    path('add_book/', views.add_book, name='add-book'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit-book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete-book'),
]
