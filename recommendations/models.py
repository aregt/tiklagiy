from django.db import models
from django.conf import settings
from products.models import Product

class Recommendation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='recommendations')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='recommendations')
    score = models.FloatField(help_text="Recommendation score between 0 and 1")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'product')
        ordering = ['-score']

    def __str__(self):
        return f"{self.user.username} - {self.product.name} ({self.score})"