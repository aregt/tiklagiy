from django.db import models
from django.conf import settings

class Store(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owned_stores')
    description = models.TextField(blank=True)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    website = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name