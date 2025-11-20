from django.shortcuts import render, get_object_or_404
from .models import Book, Library
from django.views.generic import DetailView

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})



# Class-based view for displaying library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'


    # Optionally override get_context_data if you want prefetching:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Prefetch related books to avoid extra queries if your models use ManyToMany or reverse FK
        context['books'] = self.object.books.all()  # optional: used if you prefer 'books' in template
        return context
