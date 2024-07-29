from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, UserProfile

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username', 'is_staff', 'email_verified']
    fieldsets = UserAdmin.fieldsets + (
        ('Extra Fields', {'fields': ('email_verified', 'email_verification_token')}),
    )

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'get_email']
    
    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = 'Email'

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
