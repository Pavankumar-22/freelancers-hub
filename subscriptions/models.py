from django.db import models

class Subscription(models.Model):
    CATEGORY_CHOICES = [
        ('Software', 'Software & Tools'),
        ('Cloud', 'Cloud Services'),
        ('Productivity', 'Productivity Apps'),
        ('Learning', 'Learning Platforms'),
        ('Freelancing', 'Freelancing Platforms'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    link = models.URLField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name
