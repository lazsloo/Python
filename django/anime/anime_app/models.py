from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    def user_validator(self, post_data):
        errors = {}

        if len(post_data['first_name']) < 2:
            errors['first_name'] = "Invalid weeb first name"

        if len(post_data['last_name']) < 2:
            errors['last_name'] = "Invalid weeb last name"

        users = User.objects.filter(email=post_data['email'])
        if users:
            errors['exisiting_user'] = "You're already registered weeb"

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):           
            errors['email'] = ("Invalid e-mail weeb")

        if len(post_data['username']) < 4:
            errors['username'] = "Isekai name not long enough"

        usernames = User.objects.filter(username=post_data['username'])
        if usernames:
            errors['existing_username'] = "Isekai name is already in use weeb"

        USERNAME_REGEX = re.compile(r'^[a-zA-Z0-9]')
        if not USERNAME_REGEX.match(post_data['username']):           
            errors['username'] = ("Invalid character in your Isekai name")

        if len(post_data['password']) < 6:
            errors['password'] = "Password length not long enough weeb"
        
        if post_data['password'] != post_data['confirm_pw']:
            errors['confirm_pw'] = "Missmatched password, no waifu weeb"

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    objects = UserManager()