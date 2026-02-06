# LibraryProject/bookshelf/models.py
from django.db import models

class BookShelf(models.Model):
    name = models.CharField(max_length=100)
