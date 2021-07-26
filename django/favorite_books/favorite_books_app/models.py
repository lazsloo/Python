from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    def validator(self, post_data):
        errors = {}

        if len(post_data['first_name']) <2:
            errors['first_name'] = "Enter valid first name"

        if len(post_data['last_name']) <2:
            errors['last_name'] = "Enter valid last name"

        users = User.objects.filter(email=post_data['email'])

        if users:
            errors['existing_user'] = "E-mail already in use"

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):           
            errors['email'] = "Please enter valid e-mail address"

        if len(post_data['email']) < 1:
            errors['email'] = "E-mail cannot be blank"

        if len(post_data['password']) < 8:
            errors['password'] = "Password has to be more then 8 characters"

        if post_data['password'] != post_data['confirm_pw']:
            errors['confirm_pw'] = "Password has to match"

        return errors

class BookManager(models.Manager):
    def validator(self, post_data):
        errors = {}

        if len(post_data['title']) <1:
            errors['title'] = "Must enter a title"

        if len(post_data['desc']) < 6:
            errors['desc'] = "Description must be at least 5 characters"

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Books(models.Model):
    title = models.CharField(max_length=45)
    desc = models.TextField()
    uploaded_by_id = models.ForeignKey(User, related_name="books_uploaded", on_delete=models.CASCADE)
    users_who_liked = models.ManyToManyField(User, related_name="liked_books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()
