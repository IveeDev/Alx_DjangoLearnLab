# Retrieve a Book

## Command:
```python
book = Book.objects.get(title="1984")
print(f"Title: {book.title}, Author: {book.author}, year: {book.publication_year})

## Expected Output:
```
Title: 1984, Author: George Orwell, Year: 1949
```