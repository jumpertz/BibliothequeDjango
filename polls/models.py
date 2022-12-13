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
