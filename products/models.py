from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal



class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    brand = models.CharField(max_length=100)
    fabric_type = models.CharField(max_length=100)
    pattern = models.CharField(max_length=100)
    season = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Create your models here.
