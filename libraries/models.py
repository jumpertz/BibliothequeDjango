from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200)
    synopsis = models.TextField()
    author = models.CharField(max_length=200)
    editor = models.CharField(max_length=200)
    thubnail = models.ImageField(upload_to='images/')
    pub_date = models.DateTimeField('published date')
    created_at = models.DateTimeField(auto_now_add=True)


class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)


class Library(models.Model):
    name = models.CharField(max_length=200)
    adress = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
