from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from .models import Article

@permission_required("users.can_view", raise_exception=True)
def article_list(request):
    """View all articles."""
    articles = Article.objects.all()
    return render(request, "users/article_list.html", {"articles": articles})

@permission_required("users.can_create", raise_exception=True)
def create_article(request):
    """Create an article (requires can_create permission)."""
    if request.method == "POST":
        # Handle article creation logic
        pass
    return render(request, "users/create_article.html")

@permission_required("users.can_edit", raise_exception=True)
def edit_article(request, article_id):
    """Edit an article (requires can_edit permission)."""
    article = get_object_or_404(Article, id=article_id)
    if request.method == "POST":
        # Handle article editing logic
        pass
    return render(request, "users/edit_article.html", {"article": article})

@permission_required("users.can_delete", raise_exception=True)
def delete_article(request, article_id):
    """Delete an article (requires can_delete permission)."""
    article = get_object_or_404(Article, id=article_id)
    article.delete()
    return render(request, "users/article_deleted.html")
