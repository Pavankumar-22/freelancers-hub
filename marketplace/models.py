# marketplace/models.py

from django.db import models

# Product Model (no changes, as you already have this)
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)

    def __str__(self):
        return self.name

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

# Bundled Offers Model
class BundledOffer(models.Model):
    name = models.CharField(max_length=255)
    products = models.ManyToManyField(Product, related_name='bundled_offers')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

# Freelancer Success Stories Model
class SuccessStory(models.Model):
    name = models.CharField(max_length=100)
    story = models.TextField()

    def __str__(self):
        return self.name

# Consultation Services Model
class ConsultationService(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
