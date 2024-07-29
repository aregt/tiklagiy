from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, UserProfile

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'User Profile'

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username', 'is_staff', 'email_verified']
    fieldsets = UserAdmin.fieldsets + (
        ('Extra Fields', {'fields': ('email_verified', 'email_verification_token')}),
    )
    inlines = [UserProfileInline]

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'get_email']
    
    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = 'Email'

admin.site.register(CustomUser, CustomUserAdmin)
# UserProfile'ı ayrıca kaydetmeye gerek yok, çünkü inline olarak eklendi
# admin.site.register(UserProfile, UserProfileAdmin)