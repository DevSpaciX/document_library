from django.contrib import admin

from books_app.models import Author, Book, User


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(User)