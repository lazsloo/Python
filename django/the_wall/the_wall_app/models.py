from django.db import models
import re

# Create your models here.
class MessageManager(models.Manager):
    def validator(self, post_data):

        errors = {}

        if len(post_data['content']) < 1:
            errors['content'] = "Bruh you must have something to say"

        return errors

class CommentManager(models.Manager):
    def validator(self, post_data):

        errors = {}

        if len(post_data['content']) < 1:
            errors['content'] = "Bruh you must have something to say"

        return errors

class UserManager(models.Manager):
    def validator(self, post_data):
        errors = {}

        users = User.objects.filter(email=post_data['email'])

        if users:
            errors['exisiting_user'] = "Bruh use a different email doe"

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):           
            errors['email'] = "Bruh do you know what an e-mail looks like?"

        if len(post_data['email']) < 1:
            errors['email'] = "Bruh email cannot be blank, you internet my nigga"

        if len(post_data['first_name']) < 1:
            errors['first_name'] = "Bruh yo moms must of gave you a first name"

        if len(post_data['last_name']) < 1:
            errors['last_name'] = "Bruh yo moms must of gave you a last name"

        if len(post_data['password']) < 8:
            errors['password'] = "Bruh think of it like yo gurl going find something she don't want to see"

        if post_data['password'] != post_data['confirm_pw']:
            errors['confirm_pw'] = "Bruh they gotta match dog"

        return errors

    def login_validator(self, post_data):

        errors = {}

        if len(post_data['email']) < 1:
            errors['email'] = "Bruh login can't be blank"

        if len(post_data['password']) < 8:
            errors['password'] = "Bruh invalid password bruh"

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Message(models.Model):
    content = models.TextField()
    creator = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
    users_who_liked = models.ManyToManyField(User, related_name="messages_user_liked")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    objects = MessageManager()

class Comment(models.Model):
    content = models.TextField()
    creator = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    message = models.ForeignKey(Message, related_name="comments", on_delete=models.CASCADE)
    users_who_liked = models.ManyToManyField(User, related_name="comments_user_liked")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    objects = CommentManager()