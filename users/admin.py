from django.contrib import admin
from .models import User

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_dirplay = ["id", "username", "email", "is_staff", "is_active"]
    search_fields = ["username", "first_name", "email"]
    list_filter = ["is_staff", "is_active"]
