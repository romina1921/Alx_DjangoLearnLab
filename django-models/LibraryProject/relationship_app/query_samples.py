# query_samples.py
import os
import sys
import django

# Add project directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

# Import models
from relationship_app.models import Author, Book, Library, Librarian # type: ignore

# ----- Create sample data -----
author, _ = Author.objects.get_or_create(name="J.K. Rowling")

book1, _ = Book.objects.get_or_create(title="Harry Potter 1", author=author)
book2, _ = Book.objects.get_or_create(title="Harry Potter 2", author=author)

library, _ = Library.objects.get_or_create(name="City Library")
library.books.add(book1, book2)

librarian, _ = Librarian.objects.get_or_create(name="Mr. John", library=library)

# ----- Queries -----

# 1. All books by J.K. Rowling
print("Books by J.K. Rowling:")
for book in Book.objects.filter(author=author):
    print("-", book.title)

# 2. All books in City Library
print("\nBooks in City Library:")
for book in library.books.all():
    print("-", book.title)

# 3. Librarian for City Library
librarian = Librarian.objects.get(library=library)
print("\nLibrarian for City Library:", librarian.name)
