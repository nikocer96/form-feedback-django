from django.db import models

# Create your models here.

class Review(models.Model):
    username_form = models.CharField(max_length=30)
    review_text = models.TextField()
    rating = models.IntegerField()
    