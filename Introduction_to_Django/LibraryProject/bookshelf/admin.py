from django.contrib import admin
from .models import Book


# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns to display
    list_filter = ('publication_year',)                    # Filter by year
    search_fields = ('title', 'author')                    # Search by title or author
