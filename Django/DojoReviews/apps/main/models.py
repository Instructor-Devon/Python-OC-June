from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)

    # reviews

class Book(models.Model):
    title = models.CharField(max_length=45)
    pub_date = models.DateTimeField()
    # reviews

class Review(models.Model):
    rating = models.IntegerField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    book = models.ForeignKey(Book, related_name="reviews")
    user = models.ForeignKey(User, related_name="reviews")
