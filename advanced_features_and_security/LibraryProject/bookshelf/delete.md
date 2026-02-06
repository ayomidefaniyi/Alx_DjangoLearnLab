# Delete the book

```python
from bookshelf.models import Book
b = Book.objects.get(title="Nineteen Eighty-Four")
b.delete()
Book.objects.all()
```

# Expected Output
```python
(1, {'bookshelf.Book': 1})
<QuerySet []>
```
