from django.contrib.auth.models import AbstractUser, Group, Permission, User
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
# User model


class Users(User):

    def __str__(self):
        return self.username

    @property
    def is_staff(self):
        return self.is_superuser

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    userGroups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name='user_set_custom',
        related_query_name='user',
    )
    users_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='user_set_custom',
        related_query_name='user',
    )


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

class GroupUsers(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    organizer = models.ForeignKey(Bookseller, on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)


# GroupUser model


class GroupUser(models.Model):
    group = models.ForeignKey(GroupUsers, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


# Topic model


class Topic(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


# TopicComment model


class TopicComment(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)