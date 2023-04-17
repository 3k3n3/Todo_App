from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Todo
CustomUser = get_user_model()

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("username", "email", "is_superuser")
    list_filter = ("is_superuser",)


class CustomTodoAdmin(admin.ModelAdmin):
    model = Todo
    list_display = ("title", "user", "status")
    list_filter = ("title", "user", "status")

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Todo, CustomTodoAdmin)