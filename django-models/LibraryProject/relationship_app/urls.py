from django.urls import path
from . import views


urlpatterns = [
    path('books/', views.book_list, name='list_books'),
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail')
]

