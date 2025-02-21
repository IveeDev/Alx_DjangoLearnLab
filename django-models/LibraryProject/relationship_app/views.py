from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library
from .models import Book
# Create your views here.

# Function Base View For Listing all books
def book_list(request):
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request, 'relationship_app/list_books.html', context)


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'