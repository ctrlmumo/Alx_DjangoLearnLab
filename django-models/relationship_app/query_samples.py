# relationship_app/query_samples.py
import os
import django

# --- adjust this to match your project's settings module path ---

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
    except Author.DoesNotExist:
        return []
    return list(Book.objects.filter(author=author))

def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
    except Library.DoesNotExist:
        return []
    return list(library.books.all())

def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
    except Library.DoesNotExist:
        return None
    return getattr(library, 'librarian', None)

if __name__ == "__main__":
    # Example usage (prints readable results)
    print("Books by 'George Orwell':", books_by_author("George Orwell"))
    print("Books in 'Central Library':", books_in_library("Central Library"))
    print("Librarian for 'Central Library':", librarian_for_library("Central Library"))
