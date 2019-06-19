from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)

    # faved_books

class Book(models.Model):
    title = models.CharField(max_length=45)

    favs = models.ManyToManyField(User, related_name="faved_books")