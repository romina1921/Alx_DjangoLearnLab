# CREATE
```python
from bookshelf.models import Book

book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
```

# RETRIEVE
```python
Book.objects.all()
```

# UPDATE
```python
book.title = "Nineteen Eighty-Four"
book.save()
```

# DELETE
```python
book.delete()
Book.objects.all()
```
