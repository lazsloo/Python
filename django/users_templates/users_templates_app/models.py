from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def validator(self, post_data):
        errors = {}

        if len(post_data['name']) < 5:
            errors['name'] = "User name should be at least 5 characters"

        if len(post_data['email']) < 2:
            errors['email'] = "Must have an e-mail entered"

        if len(post_data['age']) < 1:
            errors['age'] = "Bro you have to exist to make an account"

        return errors

class user(models.Model):
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()