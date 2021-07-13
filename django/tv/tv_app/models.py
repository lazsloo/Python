from django.db import models

# Create your models here.
class ShowManager(models.Manager):
    def validator(self, post_data):
        errors = {}

        if len(post_data['title']) < 2:
            errors['title'] = "Bruh show has to exist"

        if len(post_data['network']) < 3:
            errors['network'] = "Bruh network has to exist"

        if len(post_data['desc']) < 10:
            errors['desc'] = "Bruh someone must be smart enough to remember anything about the show"

        return errors

class show(models.Model):
    title=models.CharField(max_length=45)
    network=models.CharField(max_length=45)
    release=models.DateField()
    desc=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    objects = ShowManager()