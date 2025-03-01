from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from .models import Article, Book

@permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request):
    """View all articles."""
    books = Book.objects.all()
    return render(request)

@permission_required("bookshelf.can_create", raise_exception=True)
def create_book(request):
    """Create an article (requires can_create permission)."""
    if request.method == "POST":
        # Handle article creation logic
        pass
    return render(request)

@permission_required("bookshelf.can_edit", raise_exception=True)
def edit_book(request, book_id):
    """Edit an article (requires can_edit permission)."""
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        # Handle article editing logic
        pass
    return render(request)

@permission_required("bookshelf.can_delete", raise_exception=True)
def delete_book(request, book_id):
    """Delete an article (requires can_delete permission)."""
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return render("request")
