from rest_framework import serializers
from .models import Book, Author


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "author", "publication_year"]
        
        
    def validate_publication_year(self, value):
        if value > 2025:
            raise serializers.ValidationError("Publication year cannot be in the future")
        return value
        


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ["id", "name", "books"]