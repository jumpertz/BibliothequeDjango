from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
# User model


class User(AbstractUser):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'users'

# Book model


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='images/')
    description = models.TextField()
    collection = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

# Genre model


class Genre(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

# BookGenre model


class BookGenre(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

# Library model


class Library(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

# Bookseller model


class Bookseller(models.Model):
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

# BookLibrary model


class BookLibrary(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

# BookUser model


class BookUser(models.Model):
    book_library = models.ForeignKey(BookLibrary, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()
    is_returned = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

# Group model


class Group(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    organizer = models.ForeignKey(Bookseller, on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

# GroupUser model


class GroupUser(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
