from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
# books = a list of books accosiated with a given author

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author,related_name="books", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
