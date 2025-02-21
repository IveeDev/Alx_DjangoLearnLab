from django.urls import path
from .views import LibraryDetailView
from .views import book_list


urlpatterns = [
    path('books/', book_list, name='list_books'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail')
]

