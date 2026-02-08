from django import forms
from .models import Book


class ExampleForm(forms.ModelForm):
    """
    Security Note:
    This form uses Django ModelForm which automatically validates
    and sanitizes user input to prevent SQL Injection and XSS.
    """

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
