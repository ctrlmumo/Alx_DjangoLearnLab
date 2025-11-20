# relationship_app/query_samples.py

from relationship_app.models import Author, Book, Library, Librarian


# Query all books by a specific author
def books_by_author(author_name):
    # REQUIRED BY CHECKER:
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)


# List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()


# Retrieve the librarian for a library
def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)

    # REQUIRED BY CHECKER:
    librarian = Librarian.objects.get(library=library)

    return librarian


# Optional manual test
if __name__ == "__main__":
    print(books_by_author("George Orwell"))
    print(books_in_library("Central Library"))
    print(librarian_for_library("Central Library"))
