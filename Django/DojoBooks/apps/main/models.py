from django.db import models

# Create your models here.

from apps.user.models import User

    # faved_books

class Book(models.Model):
    title = models.CharField(max_length=45)

    favs = models.ManyToManyField(User, related_name="faved_books")
