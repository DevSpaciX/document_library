from django.contrib.auth.models import AbstractUser
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    is_borrowed = models.BooleanField(default=False)
    borrowed_due_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title


class User(AbstractUser):
    borrowed_books = models.ManyToManyField(Book, related_name="borrowers", blank=True)
