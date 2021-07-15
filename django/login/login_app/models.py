from django.db import models
#########
import re
# Import this for regex to make sure that e-mail is whitin parameters
#########

# Create your models here.
class UserManager(models.Manager):
    def validator(self, post_data):
        errors = {}
##########################################################
        users = User.objects.filter(email=post_data['email'])
        # This is for our e-mail to make sure there's no duplicates
##########################################################

#######################################################################
        if users:
            errors['exisiting_user'] = "Bruh use a different email doe"
            # This will give an error if there's a user in the database already
#######################################################################

##################################################################################
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):           
            errors['email'] = ("Bruh do you know what an e-mail looks like?")
# Us this format to check w/e we define is within the parameters
##################################################################################

        if len(post_data['first_name']) < 2:
            errors['first_name'] = "Bruh yo moms must of gave you a first name"

        if len(post_data['last_name']) < 2:
            errors['last_name'] = "Bruh yo moms must of gave you a last name"

        if len(post_data['password']) < 8:
            errors['password'] = "Bruh think of it like yo gurl going find something she don't want to see"

###########################################################################################################
        if post_data['password'] != post_data['confirm_pw']:
            errors['confirm_pw'] = "Bruh they gotta match dog"
        # This object is used for confirming passwords
###########################################################################################################
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    objects = UserManager()