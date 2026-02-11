"""
These views use Django REST Framework generic views to implement CRUD operations
for the Book model.

Permissions:
- List and Detail views are open to everyone.
- Create, Update, and Delete views require authenticated users.
"""
"""
BookListView supports:
- Filtering by title, author name, and publication year.
- Searching by title and author name.
- Ordering by title and publication year.

Example usage:
- /api/books/?publication_year=2020
- /api/books/?search=Harry
- /api/books/?ordering=-publication_year
"""


from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    # Add filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Fields that can be filtered
    filterset_fields = ['title', 'author__name', 'publication_year']

    # Fields that can be searched
    search_fields = ['title', 'author__name']

    # Fields that can be used for ordering
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering



# RETRIEVE one book by ID (Anyone can view)
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# CREATE a book (Only authenticated users)
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# UPDATE a book (Only authenticated users)
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# DELETE a book (Only authenticated users)
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
