from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class UserManager(models.Manager):
    def validator(self, post_data):
        errors = {}

        if len(post_data['first_name']) < 5:
            errors['first_name'] = "Bruh yo moms mustof giving you a first name"

        if len(post_data['last_name']) < 5:
            errors['last_name'] = "Bruh yo moms mustof giving you a last name"

        if len(post_data['email']) < 2:
            errors['email'] = "Do you internet?"

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    objects = UserManager()