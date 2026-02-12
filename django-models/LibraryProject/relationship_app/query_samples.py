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
from relationship_app.models import Author, Book, Library, Librarian  # type: ignore

# ----- Create sample data safely -----
author, _ = Author.objects.get_or_create(name="J.K. Rowling")

book1, _ = Book.objects.get_or_create(title="Harry Potter 1", author=author)
book2, _ = Book.objects.get_or_create(title="Harry Potter 2", author=author)

library_name = "City Library"
library, _ = Library.objects.get_or_create(name=library_name)

# Add books to library safely (avoid duplicates)
for book in [book1, book2]:
    if not library.books.filter(pk=book.pk).exists():
        library.books.add(book)

librarian, _ = Librarian.objects.get_or_create(name="Mr. John", library=library)

# ----- Queries for ALX -----

# 1. All books by J.K. Rowling
print("Books by J.K. Rowling:")
for book in Book.objects.filter(author__name="J.K. Rowling"):
    print("-", book.title)

# 2. List all books in a library
library = Library.objects.get(name=library_name)  # <-- MUST be exactly like this
print(f"\nBooks in {library_name}:")
for book in library.books.all():
    print("-", book.title)

# 3. Librarian for a library
librarian = Librarian.objects.get(library=Library.objects.get(name=library_name))  # <-- exact
print(f"\nLibrarian for {library_name}:", librarian.name)
