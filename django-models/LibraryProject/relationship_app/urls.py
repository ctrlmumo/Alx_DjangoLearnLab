from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

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
]
