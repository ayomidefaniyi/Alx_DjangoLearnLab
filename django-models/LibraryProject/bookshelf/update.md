# Update the book title

```python
from bookshelf.models import Book
b = Book.objects.get(title="1984")
b.title = "Nineteen Eighty-Four"
b.save()
b
```

# Expected Output
```python
<Book: Nineteen Eighty-Four>
```
