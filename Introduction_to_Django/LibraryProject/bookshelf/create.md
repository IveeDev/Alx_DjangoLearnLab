# Create a Book

## Command:
```python
from bookshelf.models import Book

book = Book()
book.title = "1984"
book.author = "George Orwell"
book.publication_year = 1949
book.save()
print(book)  # Expected Output: <Book: 1984>
```

## Expected Output:
```
<Book: 1984>
```
