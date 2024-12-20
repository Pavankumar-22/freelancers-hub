from django.db import models
from django.contrib.auth.models import User  # Import the User model

class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='services/',blank=True,null=True,default='services/default_service.png')
    features = models.ManyToManyField('Feature', blank=True)
    reviews = models.ManyToManyField('Review', blank=True)
    faqs = models.ManyToManyField('FAQ', blank=True)

class Feature(models.Model):
    name = models.CharField(max_length=100)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Links to the User model
    comment = models.TextField()
    rating = models.PositiveIntegerField()

class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()
