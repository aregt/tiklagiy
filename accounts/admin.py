from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, UserProfile

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username', 'phone_number', 'birth_date', 'is_staff']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserProfile)

