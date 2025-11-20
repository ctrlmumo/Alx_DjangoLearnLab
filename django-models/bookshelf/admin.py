from django.contrib import admin

# Register your models here.
from .models import Book

@admin.register(Book) #registers Book model in the admin site
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year') #defines which fields appear as columns in the list view
    list_filter = ('author', 'publication_year') #adds filter options on the right side of admin panel
    search_fields = ('title', 'author') #enables a search bar to find books by title or author