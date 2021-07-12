from django.db import models

# Create your models here.
class show(models.Model):
    title=models.CharField(max_length=45)
    network=models.CharField(max_length=45)
    release=models.DateField()
    desc=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)