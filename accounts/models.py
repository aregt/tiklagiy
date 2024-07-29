from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils.crypto import get_random_string

# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    email_verified = models.BooleanField(default=False)
    email_verification_token = models.CharField(max_length=100, blank=True)

    def generate_verification_token(self):
        return get_random_string(length=32)

    def save(self, *args, **kwargs):
        if not self.email_verification_token:
            self.email_verification_token = self.generate_verification_token()
        super().save(*args, **kwargs)

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    # Vücut ölçüleri için alanlar
    height = models.FloatField(null=True, blank=True, help_text="Boy (cm cinsinden)")
    weight = models.FloatField(null=True, blank=True, help_text="Kilo (kg cinsinden)")
    chest = models.FloatField(null=True, blank=True, help_text="Göğüs çevresi (cm cinsinden)")
    waist = models.FloatField(null=True, blank=True, help_text="Bel çevresi (cm cinsinden)")
    hips = models.FloatField(null=True, blank=True, help_text="Kalça çevresi (cm cinsinden)")

    def __str__(self):
        return f"{self.user.username}'s profile"

