from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library
# Create your views here.

# Function Base View For Listing all books
def book_list(request):
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request, 'list_books.html', context)


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'libray'