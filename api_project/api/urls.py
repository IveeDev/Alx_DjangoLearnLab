from django.urls import path, include
from .views import BookViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

# urlpatterns = [
#     path('books/', BookList.as_view(), name='book-list')
# ]