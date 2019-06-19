from django.db import models
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class UserManager(models.Manager):

    def display_detailed_values(self):
        return [ u.__dict__ for u in self.all() ]


    def register_user(self, form):
        hashed = bcrypt.hashpw(form["password"].encode(), bcrypt.gensalt())
        new_guy = self.create(first_name=form["first_name"], last_name=form["last_name"], email=form["email"], password=hashed)
        return new_guy.id

    def validate_registration(self, form):
        errors = []
        if len(form["first_name"]) < 1:
            errors.append("First Name is required")
        if len(form["last_name"]) < 1:
            errors.append("Last Name is required")
        if len(form["email"]) < 1:
            errors.append("Email field is required")
        if len(form["password"]) < 8:
            errors.append("Password must be at least 8 characters")

        if not EMAIL_REGEX.match(form["email"]):
            errors.append("Invalid Email")
       
        
        # see if we have a unique email
        result = self.filter(email=form["email"])
        if result:
            errors.append("Email already in use")

        return errors

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    catch_phrase = models.CharField(max_length=100)
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
