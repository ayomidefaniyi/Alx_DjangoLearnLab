# Create a Book instance

```python
from bookshelf.models import Book
b = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
b
```

# Expected Output
```python
<Book: 1984>
```
