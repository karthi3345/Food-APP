from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import UserProfile
from .models import Profile, UserProfile  



@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "ip_address", "city", "country", "registered_at")

admin.site.register(Profile)