from django.contrib import admin
from users.models import User
from users.forms import CustomUserCreationForm, CustomUserChangeForm


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['username', 'email', 'is_staff', 'is_active']
    search_fields = ['username', 'email']
    ordering = ['username']
