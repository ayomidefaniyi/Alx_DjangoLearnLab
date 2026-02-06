from django.db import models


class Library(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)  # ✅ simple text now
    library = models.ForeignKey(
        Library,
        on_delete=models.CASCADE,
        related_name='books'
    )

    def __str__(self):
        return self.title
