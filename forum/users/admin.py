from django.contrib import admin
from users.models import User


class AdminUser(admin.ModelAdmin):
    list_display = ("username", "is_staff")


admin.site.register(User, AdminUser)